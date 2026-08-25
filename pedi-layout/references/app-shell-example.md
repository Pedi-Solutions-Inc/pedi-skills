# Portable application shell example

This example distills the Pedi Courts implementation into portable React and Tailwind-oriented excerpts. It demonstrates component boundaries and layout behavior, not drop-in APIs. Translate component names, routing, scroll restoration, sidebar persistence, authorization, and theme tokens through the target project.

## Component map

```text
AppShell
├── AppSidebar
└── AppContent
    ├── AppSidebarHeader
    └── Breadcrumbs + Page
```

## Shell and persisted sidebar state

The shell owns sidebar state and top-level arrangement. Read the initial state from the target project's existing persistence mechanism.

```tsx
type AppShellProps = {
    children: React.ReactNode;
    sidebarInitiallyOpen: boolean;
};

export function AppShell({
    children,
    sidebarInitiallyOpen,
}: AppShellProps) {
    return (
        <SidebarProvider defaultOpen={sidebarInitiallyOpen}>
            {children}
        </SidebarProvider>
    );
}
```

## Content inset and scroll restoration

The content inset, not the document, is the vertical scroll owner. Replace `scroll-region` when the target router uses another restoration marker.

```tsx
type AppContentProps = React.ComponentProps<'main'>;

export function AppContent({
    className,
    children,
    ...props
}: AppContentProps) {
    return (
        <SidebarInset
            {...{ 'scroll-region': '' }}
            className={cn(
                'h-svh overflow-x-hidden overflow-y-auto',
                className,
            )}
            {...props}
        >
            {children}
        </SidebarInset>
    );
}
```

## Layout, header, and breadcrumbs

Pages provide breadcrumb data. The layout renders only meaningful ancestry and reduces the page's top padding when a trail is present.

```tsx
type AppSidebarLayoutProps = {
    children: React.ReactNode;
    breadcrumbs?: BreadcrumbItem[];
    sidebarInitiallyOpen: boolean;
};

export function AppSidebarLayout({
    children,
    breadcrumbs = [],
    sidebarInitiallyOpen,
}: AppSidebarLayoutProps) {
    const hasBreadcrumbs = breadcrumbs.length > 1;

    return (
        <AppShell sidebarInitiallyOpen={sidebarInitiallyOpen}>
            <AppSidebar />
            <AppContent>
                <AppSidebarHeader />
                <div
                    className={cn(
                        'flex min-h-0 flex-1 flex-col',
                        hasBreadcrumbs && '[&>[data-slot=page]]:pt-4',
                    )}
                >
                    {hasBreadcrumbs && (
                        <div className="px-4 pt-6 sm:px-8 sm:pt-8">
                            <Breadcrumbs items={breadcrumbs} />
                        </div>
                    )}
                    {children}
                </div>
            </AppContent>
        </AppShell>
    );
}
```

## Sidebar presentation

Keep authorized destinations in a separate navigation source so other surfaces, such as a command palette, can reuse them.

```tsx
export function AppSidebar() {
    const groups = useAuthorizedNavigation();

    return (
        <Sidebar collapsible="icon">
            <SidebarHeader>
                <ProductIdentity />
                <OptionalWorkspaceSwitcher />
            </SidebarHeader>

            <SidebarContent>
                {groups.map((group) => (
                    <NavigationGroup key={group.label} group={group} />
                ))}
            </SidebarContent>

            <SidebarFooter>
                <AccountSummary />
            </SidebarFooter>

            <SidebarCollapseButton />
        </Sidebar>
    );
}
```

## Sticky utility header

The mobile trigger appears in the header because the sidebar edge is absent when its sheet is closed. The desktop collapse control remains on the sidebar.

```tsx
export function AppSidebarHeader() {
    return (
        <header className="sticky top-0 z-30 flex h-14 shrink-0 items-center justify-between gap-3 border-b border-border bg-card px-4 sm:px-8">
            <div className="flex min-w-0 flex-1 items-center gap-4">
                <SidebarTrigger className="-ml-1 md:hidden" />
                <CommandAccess />
            </div>

            <div className="flex shrink-0 items-center gap-2">
                <ContextualAction />
                <AppearanceToggle />
                <Notifications />
                <AccountMenu />
            </div>
        </header>
    );
}
```

Render only utilities supported by the authenticated principal and current permissions. Hide secondary action labels at narrow widths while preserving accessible names.

## Page wrapper and sections

The shared page wrapper owns outer spacing, width, and whole-page actions. Sections own only their internal heading and local actions.

```tsx
type PageProps = {
    title?: string;
    description?: string;
    actions?: React.ReactNode;
    width?: 'full' | 'narrow';
    children: React.ReactNode;
};

export function Page({
    title,
    description,
    actions,
    width = 'full',
    children,
}: PageProps) {
    return (
        <div
            data-slot="page"
            className={cn(
                'flex flex-1 flex-col gap-8 p-4 sm:px-8 sm:py-8',
                width === 'narrow' && 'mx-auto w-full max-w-2xl',
            )}
        >
            {(title !== undefined || actions !== undefined) && (
                <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                    {title !== undefined && (
                        <PageHeading
                            title={title}
                            description={description}
                        />
                    )}
                    {actions !== undefined && (
                        <div className="flex flex-wrap items-center gap-2">
                            {actions}
                        </div>
                    )}
                </div>
            )}

            {children}
        </div>
    );
}

export function PageSection({
    title,
    actions,
    children,
}: {
    title?: string;
    actions?: React.ReactNode;
    children: React.ReactNode;
}) {
    return (
        <section className="flex flex-col gap-3">
            {(title !== undefined || actions !== undefined) && (
                <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-2">
                    {title !== undefined && <SectionHeading title={title} />}
                    {actions}
                </div>
            )}
            {children}
        </section>
    );
}
```

The excerpts intentionally omit imports and library-specific type declarations. They should be read with [app-shell.md](app-shell.md), which defines the behavioral requirements and verification states.
