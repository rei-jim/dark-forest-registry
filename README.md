# The Dark Forest Registry

A spoiler-free, star-chart character guide to Liu Cixin's **Remembrance of
Earth's Past** trilogy - *The Three-Body Problem*, *The Dark Forest*, and
*Death's End*. (Book IV is not part of this registry.)

One **tab per book**. Each book is its own constellation: characters are drawn
as stars, clustered by affiliation, and clicking a star opens a short dossier.

## The spoiler rule

Every description says only who a person is **when you first meet them in that
book** - never what they turn out to be.

- Recurring characters get a **fresh description per book**, so the Book I tab
  never leaks Book II. Luo Ji in Book II reads nothing like Luo Ji in Book III.
- No deaths, no reversals, no outcomes, no plot.
- Clusters whose *name* is itself a mid-book reveal are titled obliquely - the
  Book I faction around Mike Evans is just **"The Organization."**

One leak is structural and stated in the UI: a character listed under a later
book is, by that fact alone, still in the story then. Same trade the MDZS clan
register made with its volume dial.

## The sealed entries

Every dossier also carries a **full entry** - the complete story of that
character as of the **end** of that book, spoilers and all: deaths, betrayals,
what the twist was, what they turn out to have been doing the whole time.

It is sealed. It renders behind a dashed red panel marked ⚠ with an explicit
warning naming the character and the book, and nothing of it reaches the page
until you click. Selecting a different character or switching books **re-seals
it** - it never stays open behind your back.

The full entries respect the book boundary too: Luo Ji's Book II entry ends
where Book II ends, and says nothing about Book III.

## Features

- Three book tabs, each with its own constellation layout
- Cluster filter (dim everything but one affiliation)
- Search by name, alias, or role
- Dossier panel with affiliation, role, spoiler-free description, and a note of
  which other books the character appears in
- A sealed, manually-opened **full entry** per character per book (see below)
- Deterministic layout - no randomness, so the chart never reshuffles
- **Responsive**: the constellation measures its container and lays itself out
  for the real width, so on a phone it becomes one cluster per row at readable
  1:1 type rather than a shrunken 1080px chart

## What this repo is

The chart is a **React** component. Streamlit is Python and can't run JSX
directly, so it ships as a single self-contained HTML file
(`app_component.html`) that loads React and Babel from CDNs - no build step -
and `streamlit_app.py` embeds it.

```
three-body-character-dict/
├── streamlit_app.py       # Streamlit entrypoint (embeds the HTML)
├── app_component.html     # the whole app, self-contained (edit CAST here)
├── .streamlit/
│   └── config.toml        # dark theme + bind to localhost only
├── requirements.txt
├── README.md
└── .gitignore
```

You can also just open `app_component.html` in a browser - it needs no server.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate             # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Opens at http://localhost:8501. (Requires internet - React, Babel and the
Google fonts load from CDNs.)

## Editing the data

Two objects near the top of `app_component.html`:

- **`CLUSTERS`** - the affiliations: display name, hanzi glyph, colour, and an
  optional `note` shown under the heading in the contents panel.
- **`CAST`** - one entry per character:

```js
{ id: "luoji", name: "Luo Ji", aka: "…", books: {
    2: { cluster: "wallfacer", role: "astronomer, then sociologist",
         desc: "…",          // safe: who he is when you meet him in Book II
         spoiler: "…" },     // sealed: everything, through the end of Book II
    3: { cluster: "sci", role: "an old man", desc: "…", spoiler: "…" },
}}
```

Presence of a book number = the character appears in that book. Each book gets
its own `cluster`, `role`, `desc` and `spoiler`, which is what keeps the tabs
spoiler-tight. `spoiler` is optional - omit it and the seal simply doesn't
render for that entry. Layout is computed from the data - add a character and
the constellation re-packs itself.

> When adding entries, bias every description **earlier** than you think you
> need to. If a sentence would only make sense to someone who has finished the
> book, it does not belong.

## Deploy on Streamlit Community Cloud (free)

1. Push this folder to a GitHub repo.
2. Go to https://share.streamlit.io → **Create app** → deploy from GitHub.
3. **Main file path** = `streamlit_app.py`. Deploy.

Every push to `main` redeploys automatically.
