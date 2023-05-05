# ProtoCSS
ProtoCSS is a powerful and easy-to-use superset of CSS that provides a streamlined solution for converting ProtoCSS code into standard CSS. It simplifies the handling of variables, shorthand properties, and other unique features of the ProtoCSS language, while allowing for seamless integration with vanilla CSS. ProtoCSS is designed for speed and efficiency, making it a great choice for developers who want to streamline their workflows.

## Features
* Converts ProtoCSS code to standard CSS.
* Simplifies handling of variables, shorthand properties, and other unique features of ProtoCSS language.
* Provides seamless integration with vanilla CSS.
* Handles variable substitution and shorthand property expansion.
* Offers exceptional ease of use for developers of all skill levels.
* Provides high speed and efficiency for streamlined workflows.

## Examples

``` css
/* Base styles */
@fs: 16px;
@ff: "Roboto", sans-serif;
@c: #333;
@!blue: #2196F3;

/* Layout */
.container {
    @w: 80%;
    @m: 0 auto;
    @c: %!blue;
}

.header {
    @bg: #f5f5f5;
    @p: 20px 0;
    @d: flex;
    @jc: space-between;
    @ai: center;
}
```
This will output the following CSS:

``` css
:root {
--blue: #2196F3;
--red: #f44336;
}

/* Base styles */
font-size: 16px;
font-family: "Roboto", sans-serif;
color: #333;


/* Layout */
.container {
    width: 80%;
    margin: 0 auto;
    color: var(--blue);
}

.header {
    background-color: #f5f5f5;
    padding: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```
## Contributing
Contributions to ProtoCSS are welcome! Please see our contributing guidelines for more information.

## License
ProtoCSS is released under the MIT License.
