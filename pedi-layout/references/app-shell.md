# Application shell

## Provenance and scope

This reference distills the reusable structure of Pedi Courts' authenticated application shell. The guidance in this document is self-contained and is the authoritative layout direction for this skill.

The original application implementation is provenance only, not a runtime or installation dependency. Its routes, authentication shape, branch model, roles, and menus are not part of this skill's contract.

For portable React and Tailwind-oriented component excerpts, read [app-shell-example.md](app-shell-example.md). The example retains the structural decisions described here while omitting product-specific behavior.

## Composition

Use this structural order for authenticated application workspaces:

```text
App shell / sidebar state provider
├── App sidebar
│   ├── Brand and application identity
│   ├── Optional scope or workspace switcher
│   ├── Grouped primary navigation
│   ├── Account footer
│   └── Desktop collapse control
└── Content inset (the vertical scroll owner)
    ├── Sticky utility header
    │   ├── Mobile sidebar trigger and search/command access
    │   └── Contextual action, appearance, notifications, account
    └── Flexible vertical page region
        ├── Breadcrumbs, when the trail has meaningful ancestry
        └── Page
            ├── Title, description, and page-level actions
            └── Sections and task content
```

The shell composes these pieces but does not know menu entries or page content. Pages supply breadcrumbs through the target framework's normal layout-prop mechanism.

## Shell and scrolling

For the sidebar variant, the shell provides sidebar state and arranges sidebar and content as one full-width flex row. Restore the last expanded/collapsed choice through the project's existing server, cookie, or client persistence mechanism.

The content inset is the application's single vertical scroll region:

- Use the small-viewport height unit (`svh`) when supported so mobile browser chrome does not create an oversized shell.
- Hide horizontal overflow at the inset; individual tables or canvases may own deliberate horizontal scrolling.
- Mark the inset as the router's scroll-restoration region when required. In Pedi Courts this is Inertia's `scroll-region` attribute.
- Keep the header inside the inset and sticky at its top. Use an opaque semantic surface, a bottom border, and sufficient stacking order to remain legible as content scrolls underneath.
- Let the region below the header use `min-height: 0`, `flex: 1`, and column direction so nested tables and panels can shrink and scroll correctly.

Avoid simultaneous document and inset scrolling. Nested vertical scroll regions make sticky behavior, keyboard navigation, and route restoration unpredictable.

## Sidebar direction

The app sidebar is persistent on desktop and an off-canvas sheet on mobile.

- Expanded desktop width in the reference is `16.25rem`; collapsed icon width is `3rem`. Treat these as starting proportions and preserve target-project primitives when already defined.
- Arrange the sidebar vertically: brand at the top, optional operating scope below it, navigation in the flexible middle, and account identity in the footer.
- Group navigation by user intent or responsibility. Keep its data source separate from rendering so the same authorized destinations can feed a command palette or another navigation surface.
- Keep active state visible through background, text weight, and icon treatment rather than relying on color alone.
- When a group contains the current page, it must remain open. When the sidebar collapses to icons, keep every destination reachable and expose labels through accessible tooltips.
- Put the desktop collapse control on the sidebar edge because it acts on the sidebar. Put the mobile trigger in the sticky header because the sidebar edge is absent while the sheet is closed.
- Do not show both controls at the same breakpoint.

The brand area should communicate product identity and, when useful, the current app context. A scope switcher belongs near the top only when the user can actually change organization, branch, workspace, or an equivalent context.

## Header direction

The sticky header is a compact global utility bar, not a second navigation system.

- Keep it a single row with a stable height; the reference bar is `3.5rem` (`h-14`).
- The leading side contains the mobile sidebar trigger and global find/command access.
- The trailing side contains at most one contextual high-value shortcut followed by global utilities such as appearance, notifications, and account.
- Allow the leading group to shrink (`min-width: 0; flex: 1`) and keep the utility group from shrinking.
- Hide secondary action labels before their icons on narrow screens, while retaining an accessible name.
- Render utilities only when the authenticated principal and permissions support them.

Do not repeat breadcrumbs, the page title, or desktop sidebar collapse controls in this bar.

## Breadcrumb direction

Breadcrumbs sit between the header and page content. They clarify ancestry; they do not restate a single current-page label.

- Render the trail only when it contains more than one item.
- Align its horizontal padding with the page wrapper: compact on mobile and roomier from the small breakpoint upward.
- When breadcrumbs appear, reduce duplicate vertical whitespace before the page header. In the reference implementation the layout adjusts the page's top padding instead of making each page do it.
- Keep breadcrumb generation with the page or route, not embedded in the shell.

## Page and content direction

All app pages flow vertically through a shared page wrapper.

- Use compact outer padding on phones, larger horizontal and vertical padding from the small breakpoint, and a clear vertical gap between major children.
- Put the title and description on the leading side and screen-wide actions on the trailing side. Stack them on small screens and align them in one row when space permits.
- Let actions wrap instead of overflowing. Put only actions affecting the whole screen in the page header.
- Use full width for tables, calendars, charts, dashboards, and dense operational views.
- Center narrow forms and focused tasks in a readable column; the reference maximum is approximately `42rem` (`max-w-2xl`).
- Separate major sections more than the elements inside a section. The reference rhythm is roughly `2rem` between page children and `0.75rem` within a section.
- Headings carry no outer margin. Their parent wrapper owns spacing so margins do not compound.
- A section may have its own title, description, and local actions, but it must not recreate the page header.

Representative direction:

```text
Page
├── Page header
│   ├── Title + optional description
│   └── Whole-page actions
├── Summary / status
├── Primary work area
└── Supporting sections
    ├── Section heading + local action
    └── Section content
```

## Choosing this shell

Use the app sidebar shell when authenticated users move repeatedly among several work areas and need persistent context. Choose another established layout for:

- public discovery or marketing pages;
- sign-in, registration, and recovery;
- focused onboarding or checkout;
- long-form policy or help reading;
- an app with only a few top-level destinations that already has a successful header-navigation shell.

## Verification matrix

Check the states that exist in the target product:

| Area | States |
| --- | --- |
| Sidebar | expanded desktop, collapsed desktop, mobile sheet open/closed |
| Navigation | active route, nested active route, collapsed group, long labels, permission-filtered groups |
| Header | utility-rich account, restricted account, narrow width, sticky over scrolling content |
| Breadcrumbs | none, single item, multi-item, long item labels |
| Page | short page, long page, narrow form, wide table/chart, wrapped actions |
| Theme/input | light, dark, keyboard focus, reduced viewport height |

Verify that route changes reset or restore the content inset's scroll position according to product behavior, not the browser document's stale position.
