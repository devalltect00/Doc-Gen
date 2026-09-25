<!-- docs/architecture/design-patterns.md -->

# Design Patterns

This document explains design patterns used in the DocGen project.

---

## Registry and Composition Pattern

Project detection produces a fingerprint with one compatible primary type and
multiple ecosystem, framework, and tool signals. The metadata registry merges
common documentation with increasingly specific catalogs.

Benefits:

- Mixed-stack repositories are represented without a combinatorial enum
- New ecosystems and frameworks can extend metadata independently
- Existing CLI and configuration values remain compatible
- Detection, metadata, rendering, and ignore behavior remain testable

---

## Service Layer Pattern

Core services isolate responsibilities.

Examples:

- StructureGenerator
- ProjectAnalyzer
- TreePrinter

Benefits:

- Maintainability
- Separation of concerns
- Reusable logic

---

## Builder Pattern

The builder pattern is used for constructing complex output.

`StructureConfigBuilder` resolves the backend configuration used by scanners.

Benefits:

- Clean construction logic
- Reusable builders
- Clear separation of concerns

---

## DTO / Data Model Pattern

Structured result objects are implemented using dataclasses.

Example:

```python
ProjectFingerprint
AnalysisResult
GenerationResult
```

Benefits:

- Predictable structure
- Easier testing
- Cleaner APIs

---

## Composition Over Inheritance

The project prefers composition where possible.

Example:

```python
MarkdownGenerator
    -> ScannerService
    -> MetadataRegistry
    -> Section renderers
```

Instead of deep inheritance trees.

---

## Why These Patterns?

The project is designed to remain:

- Easy to extend
- Easy to test
- Easy to maintain
- Language-independent
