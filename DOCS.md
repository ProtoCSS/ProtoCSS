# ProtoCSS Documentation
Welcome to the ProtoCSS! To get started, you will need to clone the repository from the official Github page.

Once you have cloned the repository, you can import the necessary modules and create an instance of the ProtoCSS class to begin using the preprocessor.

The ProtoCSS Preprocessor is designed to enhance your workflow by seamlessly integrating with vanilla CSS and simplifying the handling of variables, shorthand properties, and other unique features of the ProtoCSS language. With ProtoCSS, you can write cleaner, more efficient code with less repetition, allowing you to streamline your workflow and enhance your productivity.

We recommend exploring the provided examples and documentation to get a better understanding of the capabilities of the ProtoCSS Preprocessor. If you encounter any issues or have any questions, please refer to the official Github page for support.

## Features
The ProtoCSS preprocessor offers a comprehensive set of user-friendly features designed to enhance the experience of working with CSS for developers of all skill levels. These features include:

* **Streamlined Imports:** Easily import external CSS and ProtoCSS files using Python-style import statements, managing various file types and handling errors effectively.
* **Efficient Variable Handling:** Simplify working with dynamic values using ProtoCSS variables, which are seamlessly converted and used within your code.
* **List Support:** Define and manage lists in your ProtoCSS code, allowing for easy storage and retrieval of grouped data. This can be highly useful for color schemes, font stacks, and more.
* **For Loop Support:** Iteratively generate CSS rules with varying properties using ProtoCSS for loop syntax. This can be especially useful for creating theme variants, responsive designs, or any other rule sets that follow a consistent pattern.
* **Reusable Style Groups:** Create and utilize style groups to minimize repetition and improve maintainability within your CSS code.
* **Shorthand Property Expansion:** Save time and effort by employing shorthand properties, which are automatically expanded to their full equivalents by the preprocessor.
* **Media Query Simplification:** Leverage the `@mq` keyword for a more concise and readable method of defining media queries.
* **Flexible Integration:** Effortlessly blend the advanced features of ProtoCSS with standard CSS code, providing a seamless integration experience.
* **Enhanced Efficiency:** Benefit from the high speed and efficiency of the ProtoCSS preprocessor, optimizing your workflow for maximum productivity.

These accessible and powerful features make the ProtoCSS preprocessor an exceptional choice for developers seeking to streamline their CSS development process.

## Examples
Here is an example of using ProtoCSS to convert a mixed ProtoCSS and vanilla CSS code into standard CSS:
``` css
import "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700"; /* Example for web import */
import "header.css"; /* Example for direct .css import */
import "header.ptcss"; /* Example for direct .ptcss import */
import "footer"; /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


/* Base styles */
@fs: 16px;
@ff: "Roboto", sans-serif;
@c: #333;
@!blue: #2196F3;

/* List below */
list@colors: ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black"];
list@widths: [25%, 50%, 75%, 100%];

for width in widths {
    #logo {
        @c: black;
        width: {width};
        @p: 20px 0;
        @d: flex;
        @jc: space-between;
        @ai: center;
    }
};

/* For loop above */

/* Layout */
.container {
    @w: 80%;
    margin: 0 auto;
    @c: %!blue; /* Example for variable usage */
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
```

This is equivalent to:
``` css
:root {
--blue: #2196F3;
--red: #f44336;
}

@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700"); /* Example for web import */
@import url("static/css/header.css"); /* Example for direct .css import */
@import url("static/css/header.css"); /* Example for direct .ptcss import */
@import url("static/footer.ptcss"); /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


/* Base styles */
font-size: 16px;
font-family: "Roboto", sans-serif;
color: #333;

/* List below */

#logo-25 {
   color: black;
   width: 25%;
   padding: 20px 0;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

#logo-50 {
   color: black;
   width: 50%;
   padding: 20px 0;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

#logo-75 {
   color: black;
   width: 75%;
   padding: 20px 0;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

#logo-100 {
   color: black;
   width: 100%;
   padding: 20px 0;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

/* For loop above */

/* Layout */
.container {
    width: 80%;
    margin: 0 auto;
    color: var(--blue); /* Example for variable usage */
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
```
This example showcases the ability of the ProtoCSS Preprocessor to handle imports, variables, shorthand properties, lists and a for loop.

## Supported Properties
The ProtoCSS Preprocessor is designed to offer a comprehensive set of shorthand properties and CSS attributes, making it easier for developers to efficiently create and maintain styles. By providing a robust set of features, ProtoCSS allows you to focus on creating visually stunning and highly functional designs with greater ease and simplicity.

In order to make your styling process more streamlined, the ProtoCSS Preprocessor supports an extensive list of shorthand properties. These shorthand properties help you write concise and easily understandable code, resulting in a more maintainable and efficient workflow.

The following table showcases the shorthand properties currently supported:
### Basic Properties
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

## Lists
In ProtoCSS, lists are a way to group data that belongs together. They can be used to store a set of values, such as colors, font stacks, or breakpoints.

### Defining a List
To define a list in ProtoCSS, you can use the `list@` syntax, followed by the name of the list and its contents enclosed in square brackets. Here's an example:

``` css
list@colors: ["red", "green", "blue"];
```
In this example, we've defined a list called `colors` that contains three color values.

### Using a List
Once you've defined a list, you can use it throughout your ProtoCSS code by referencing its name. You can access individual items in the list using square bracket notation and an index. The index starts at zero, so the first item in the list has an index of 0, the second item has an index of 1, and so on.

Here's an example that uses the colors list we defined earlier:

``` css
.box {
  @c: list@colors[0];
}
```

In this example, we've applied a background color to a box element using the first color in the colors list.

You can also use the for loop syntax to iterate over a list and generate a set of CSS rules for each item. Here's an example that uses the colors list again:

``` css
for color in colors {
  .container {
    @c: {color};
  }
}
```
In this example, we're using a for loop to generate a set of CSS rules for each color in the colors list. The @{color} syntax is used to access the current color value in the loop and interpolate it into the CSS rule.

## For loops
The `for` loop is a powerful feature of ProtoCSS that enables you to generate CSS rules with varying properties. This can be especially useful for creating theme variants, responsive designs, or any other rule sets that follow a consistent pattern.

Here's an example of how you can use a `for` loop in ProtoCSS:

``` css
list@colors: ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black"];

for color in colors {
    .color {
        @bg: {color};
        @c: white;
        padding: 10px;
    }
}
```

In this example, we have defined a list called `colors`, which contains ten color values. We then use a for loop to iterate over the list and generate a set of CSS rules for each color. The `{}` syntax is used to interpolate the value of the color variable into the generated CSS rule, resulting in the creation of ten color classes with varying background colors.

The resulting CSS output would look like this:

``` css
.color-red {
    background-color: red;
    color: white;
    padding: 10px;
}

.color-green {
    background-color: green;
    color: white;
    padding: 10px;
}

.color-blue {
    background-color: blue;
    color: white;
    padding: 10px;
}

/* ...and so on for all ten colors */
```

As you can see, using a for loop in ProtoCSS can greatly simplify the process of generating repetitive CSS rules, and can be used in a wide range of scenarios.
