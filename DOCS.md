# ProtoCSS Framework Documentation
Welcome to the ProtoCSS Framework! To get started, you will need to clone the repository from the official Github page.

Once you have cloned the repository, you can import the necessary modules and create an instance of the ProtoCSS class to begin using the framework.

The ProtoCSS Framework is designed to enhance your workflow by seamlessly integrating with vanilla CSS and simplifying the handling of variables, shorthand properties, and other unique features of the ProtoCSS language. With ProtoCSS, you can write cleaner, more efficient code with less repetition, allowing you to streamline your workflow and enhance your productivity.

We recommend exploring the provided examples and documentation to get a better understanding of the capabilities of the ProtoCSS Framework. If you encounter any issues or have any questions, please refer to the official Github page for support.

## Examples
Here is an example of using the ProtoCSS Framework to convert a mixed ProtoCSS and vanilla CSS code into standard CSS:
``` css
import "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700"; /* Example for web import */
import "header.css"; /* Example for direct .css import */
import "header.prot"; /* Example for direct .prot import */
import "footer"; /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


@fs: 16px;
@ff: "Roboto", sans-serif;
@c: #333;
@!blue: #2196F3; /* Example for variable assignment, can be placed anywhere in the code */

/* Example for mixed ProtoCSS & Vanilla CSS */
.container {
    @w: 80%;
    margin:: 0 auto;
    @c: %!blue; /* Example for variable usage */
}
```

This is equivalent to:
``` css
:root {
--blue: #2196F3;
--red: #f44336;
}

@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700"); /* Example for web import */
@import url("static/css/header.css"); /* Example for direct .css import */
@import url("static/css/header.css"); /* Example for direct .prot import */
/* Error: Invalid import 'footer'. */ 
@import url("static/css/header.css"); /* Example for vanilla css import support */


font-size: 16px;
font-family: "Roboto", sans-serif;
color: #333;
 /* Example for variable assignment, can be placed anywhere in the code */

/* Example for mixed ProtoCSS & Vanilla CSS */
.container {
    width: 80%;
    margin:: 0 auto;
    color: var(--blue); /* Example for variable usage */
}
```
This example showcases the ability of the ProtoCSS Framework to handle imports, variables, shorthand properties, and variable usage.

## Supported Properties
The ProtoCSS Framework provides a comprehensive list of shorthand properties and CSS attributes to simplify the styling process.

Here is a table of the shorthand properties that the ProtoCSS currently supports:
## Basic Properties
|ProtoCSS Syntax|CSS Property Equivalent|
|:---: | :---: |
|@bg|background-color|
|@c|color
|@fs|font-size
|@ff|font-family
|@fw|font-weight
|@lh|line-height
|@m|margin
|@mt|margin-top
|@mr|margin-right
|@mb|margin-bottom
|@ml|margin-left
|@p|padding
|@pt|padding-top
|@pr|padding-right
|@pb|padding-bottom
|@pl|padding-left
|@w|width
|@h|height
|@br|border-radius
|@bc|border-color
|@bs|border-style
|@bw|border-width

### Layout Properties
|ProtoCSS Syntax|CSS Property Equivalent|
|:---: | :---: |
|@d|display
|@jc|justify-content
|@flx|flex
|@fld|flex-direction
|@flw|flex-wrap
|@flg|flex-grow
|@fls|flex-shrink
|@flb|flex-basis
|@ai|align-items
|@ac|align-content
|@as|align-self
|@fl|float
|@pos|position
|@t|top
|@r|right
|@b|bottom
|@l|left
|@z|z-index

### Text Properties
|ProtoCSS Syntax|CSS Property Equivalent|
|:---: | :---: |
|@op|opacity
|@o|outline
|@ov|overflow
|@ta|text-align
|@td|text-decoration
|@ti|text-indent
|@tt|text-transform
|@va|vertical-align
|@whs|white-space
|@ws|word-spacing
|@v|visibility
|@lst|list-style-type
|@ls|letter-spacing

### Background and Border Properties
|ProtoCSS Syntax|CSS Property Equivalent|
|:---: | :---: |
|@bgp|background-position
|@bgr|background-repeat
|@bgs|background-size
|@bgimg|background-image
|@tsh|text-shadow
|@bxsh|box-shadow
|@tr|transition
|@bo|border
|@br|border-radius
|@bc|border-color
|@bs|border-static
|@bw|border-width
|@olc|outline-color
|@olw|outline
