# ProtoCSS Documentation
Welcome to the ProtoCSS! To get started, you will need to clone the repository from the official Github page.

Once you have cloned the repository, you can import the necessary modules and create an instance of the ProtoCSS class to begin using the preprocessor.

The ProtoCSS Preprocessor is designed to enhance your workflow by seamlessly integrating with vanilla CSS and simplifying the handling of variables, shorthand properties, and other unique features of the ProtoCSS language. With ProtoCSS, you can write cleaner, more efficient code with less repetition, allowing you to streamline your workflow and enhance your productivity.

We recommend exploring the provided examples and documentation to get a better understanding of the capabilities of the ProtoCSS Preprocessor. If you encounter any issues or have any questions, please refer to the official Github page for support.

## Features
The ProtoCSS preprocessor offers a comprehensive set of user-friendly features designed to enhance the experience of working with CSS for developers of all skill levels. These features include:

* **Streamlined Imports:** Easily import external CSS and ProtoCSS files using Python-style import statements, managing various file types and handling errors effectively.
* **Efficient Variable Handling:** Simplify working with dynamic values using ProtoCSS variables, which are seamlessly converted and used within your code.
* **Reusable Style Groups:** Create and utilize style groups to minimize repetition and improve maintainability within your CSS code.
* **Shorthand Property Expansion:** Save time and effort by employing shorthand properties, which are automatically expanded to their full equivalents by the preprocessor.
* **Media Query Simplification:** Leverage the @mq keyword for a more concise and readable method of defining media queries.
* **Flexible Integration:** Effortlessly blend the advanced features of ProtoCSS with standard CSS code, providing a seamless integration experience.
* **Enhanced Efficiency:** Benefit from the high speed and efficiency of the ProtoCSS preprocessor, optimizing your workflow for maximum productivity.

These accessible and powerful features make the ProtoCSS preprocessor an exceptional choice for developers seeking to streamline their CSS development process.

## Examples
Here is an example of using ProtoCSS to convert a mixed ProtoCSS and vanilla CSS code into standard CSS:
``` css
import "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700"; /* Example for web import */
import "header.css"; /* Example for direct .css import */
import "header.prt"; /* Example for direct .prt import */
import "footer"; /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


/* Base styles */
@fs: 16px;
@ff: "Roboto", sans-serif;
@c: #333;
@!blue: #2196F3;

/* Layout */
.container {
    @w: 80%;
    margin:: 0 auto;
    @c: %!blue; /* Example for variable usage */
}

.container {
    @w: 100%;
    @p: 10px;
}


group@blueishPack {
    @m: 0;
    @c: white;
    @br: 10px;
}

.header {
    group@blueishPack;
    @bg: #f5f5f5;
    @p: 20px 0;
    @d: flex;
    @jc: space-between;
    @ai: center;
}

/* Navigation */
.nav {
    @d: flex;
    group@blueishPack;
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
@import url("static/css/header.css"); /* Example for direct .prt import */
@import url("static/footer.prt"); /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


/* Base styles */
font-size: 16px;
font-family: "Roboto", sans-serif;
color: #333;


/* Layout */
.container {
    width: 80%;
    margin:: 0 auto;
    color: var(--blue); /* Example for variable usage */
}

.container {
    width: 100%;
    padding: 10px;
}




.header {
    margin: 0;
    color: white;
    border-radius: 10px;
    background-color: #f5f5f5;
    padding: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Navigation */
.nav {
    display: flex;
    margin: 0;
    color: white;
    border-radius: 10px;
}



.nav-item {
    margin: 0 10px;
    font-size: 14px;
    color: var(--blue);
}
```
This example showcases the ability of the ProtoCSS Preprocessor to handle imports, variables, shorthand properties, and variable usage.

## Supported Properties
The ProtoCSS Preprocessor is designed to offer a comprehensive set of shorthand properties and CSS attributes, making it easier for developers to efficiently create and maintain styles. By providing a robust set of features, ProtoCSS allows you to focus on creating visually stunning and highly functional designs with greater ease and simplicity.

In order to make your styling process more streamlined, the ProtoCSS Preprocessor supports an extensive list of shorthand properties. These shorthand properties help you write concise and easily understandable code, resulting in a more maintainable and efficient workflow.

The following table showcases the shorthand properties currently supported:
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
