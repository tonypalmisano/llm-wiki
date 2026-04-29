# Optional PDF Ingestion With OpenDataLoader PDF

LLM Wiki is Markdown-first. Plain Markdown ingestion remains the default
fallback, and the core project stays dependency-free.

OpenDataLoader PDF can be used as an optional preprocessing step for PDF-based
sources. It can convert PDFs into Markdown for normal LLM Wiki ingestion and
preserve JSON layout metadata with page numbers and bounding boxes for stronger
source traceability.

This repository does not vendor OpenDataLoader PDF source code, does not add it
as a global dependency and does not require it for the core workflow.

## Runtime Requirements

OpenDataLoader PDF may require:

- Java 11+
- Python 3.10+

Before using it, verify Java is available:

```bash
java -version
```

## Optional Installation

Basic PDF conversion:

```bash
pip install -U opendataloader-pdf
```

Hybrid/OCR features:

```bash
pip install "opendataloader-pdf[hybrid]"
```

Do not add these packages to the repository root as global requirements.

## Why Batch Conversion Is Recommended

OpenDataLoader PDF conversion can start a JVM process. Batch conversion is
therefore preferred over repeatedly converting one file at a time.

Use one conversion run for multiple PDFs when possible.

## Output Formats Relevant To LLM Wiki

Useful outputs include:

- Markdown: primary human-readable source for normal LLM Wiki ingest.
- JSON: structured layout metadata, including page numbers and bounding boxes.
- HTML or text: optional secondary inspection formats.
- Annotated PDF: optional visual debugging output.

For LLM Wiki, the most useful pair is:

```text
format="markdown,json"
```

## Recommended Raw Layout

Keep original PDFs and converted artifacts separate:

```text
raw/
  inbox/
    source.pdf
  converted/
    source-id/
      document.md
      document.json
      annotated.pdf
      manifest.md
  processed/
```

Recommended artifact names:

- `document.md`: converted Markdown used for wiki ingest.
- `document.json`: layout metadata with pages, elements and bounding boxes.
- `annotated.pdf`: optional visual debugging artifact.
- `manifest.md`: conversion notes, command, date, tool version if known and limitations.

## Ingest Flow

1. Place the original PDF under `raw/inbox/`.
2. Convert it with OpenDataLoader PDF into `raw/converted/<source-id>/`.
3. Ingest `raw/converted/<source-id>/document.md` using the normal LLM Wiki workflow.
4. Create or update a source page under `wiki/sources/`.
5. Reference the original PDF and converted artifacts from the source page.

Example source page references:

```md
Raw PDF: `raw/inbox/source.pdf`
Converted Markdown: `raw/converted/source-id/document.md`
Layout metadata: `raw/converted/source-id/document.json`
```

## Claim Source References With Page And Bounding Box Metadata

OpenDataLoader JSON metadata can support more precise claim references.

A synthesis claim can cite:

- the wiki source page;
- the PDF page number;
- the JSON element ID if available;
- the bounding box when precision is useful.

Example claim table rows:

```md
| ID | Claim | Type | Source refs | Support status | Confidence | Review status |
|---|---|---|---|---|---|---|
| C1 | The report says temporary retrieval does not create durable structure. | factual | [[sources/source-id]] p. 3 bbox [72,400,540,650] | supported | medium | needs_review |
| C2 | The table lists three evaluation categories. | factual | [[sources/source-id]] p. 7 element 42 | supported | high | reviewed |
```

These references are review aids, not proof. Humans should still inspect the
source when accuracy matters.

## Privacy And Trust Caveats

OpenDataLoader PDF can run locally, but users should still review their selected
mode and dependencies.

Important caveats:

- OCR and hybrid modes may add more moving parts than basic Markdown conversion.
- AI-assisted enrichment can produce imperfect descriptions or interpretations.
- Extracted page numbers and bounding boxes can be precise while the extracted
  content is still wrong.
- Sensitive PDFs should be handled according to local privacy and security
  requirements.
- LLM Wiki does not certify the truth of converted content or extracted claims.

## Out Of Scope

This integration note does not add:

- OpenDataLoader PDF as a core dependency;
- repository-level `requirements.txt`;
- vendored OpenDataLoader PDF source code;
- converter scripts;
- Java or Python environment management;
- OCR/hybrid server orchestration;
- JSON/JSONL export pipelines;
- databases, embeddings or external services;
- PDF/UA accessibility remediation;
- CI checks that require Java or OpenDataLoader PDF.

Plain Markdown ingestion remains the default fallback.
