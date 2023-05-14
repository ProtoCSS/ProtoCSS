# Changelog

All notable changes to the ProtoCSS project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1]-dev - 2023-05-13

### Added

- First official release of the ProtoCSS preprocessor - **still in development**, but ready for use.
- **Variables:** Support for simplified ProtoCSS variables for easy handling of dynamic values.
- **Shorthands:** Shorthand properties that are automatically expanded to their full property equivalents.
- **PD Shorthands:** Support for property-declaration shorthand properties, which are automatically expanded to their full equivalents.
- Seamless integration with vanilla CSS.
- **Import:** Ability to import external CSS and ProtoCSS files using Python-styled `import` statements.
- **Mixins:** Reusable style mixins to avoid repetition and improve maintainability.
- **Lists:** Support for defining and managing lists, enabling easy storage and retrieval of mixin data such as color schemes and font stacks.
- **For loops:** Introduced for loops, allowing for the iterative generation of CSS rules with varying properties, greatly enhancing the ability to create theme variants, responsive designs, and consistent patterned rule sets.
- **Conditions:** Native support for JS-like conditional statements, enabling dynamic styling based on defined conditions for more flexible and responsive design solutions.
- File change watcher feature that automatically detects and processes changes in ProtoCSS files, ensuring the CSS stays up-to-date without manual intervention.
- Robust error handling for catching and providing detailed information on any errors that occur during the preprocessing step, facilitating quick debugging and problem resolution.
- SEMVER: ensuring consistency and clarity in versioning.
- Improved efficiency for streamlined workflows.
- Comprehensive documentation, covering various features and helping users get the most out of ProtoCSS.