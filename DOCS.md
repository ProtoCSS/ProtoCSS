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
* **Reusable Style Mixins:** Create and utilize style mixins to minimize repetition and improve maintainability within your CSS code.
* **Conditional Support:** Utilize the power of "if-else" conditional statements natively supported by ProtoCSS. Apply different styles based on specific conditions, offering more dynamic and versatile CSS coding. This feature enhances flexibility and responsiveness in design solutions, catering to a wide range of use-cases and scenarios.
* **Shorthand Property Expansion:** Save time and effort by employing shorthand properties, which are automatically expanded to their full equivalents by the preprocessor.
* **Property-Declaration Shorthands:** Take advantage of Property-Declaration shorthand properties in ProtoCSS, allowing you to write fast, concise and expressive code without sacrificing flexibility.
* **File Change Watcher:** ProtoCSS includes a file watcher that automatically detects and processes changes in your code. This feature ensures your CSS stays up-to-date without manual intervention.
* **Error Management:** ProtoCSS includes robust error management, catching and providing detailed information on any errors that occur during the preprocessing step. This functionality allows for quick debugging and problem resolution.
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

.example {
    @w: list@widths[0];
    @w: list@widths[1];
    @w: list@widths[2];
    @w: list@widths[3];
    @w: list@widths[4]; /* Example for error */
    @w100; /* Example for predefined shorthand */
}

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

/* Predefined shorthands */
.main-container {
    @w100;
    @p20;
    @df;
    @jcsb;
}

/* Layout */
.container {
    @w: list@widths[0]; /* Example for list access usage */
    @tdn; /* Example for predefined shorthand */
    @c: %!blue; /* Example for variable usage */
}

mixin@blueishPack {
    @w100;
    @c: white;
    @br: 10px;
}

.header {
    mixin@blueishPack;
    @bg: #f5f5f5;
    @tdn;
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
/* Error: File 'header.ptcss' not found in static/. */ /* Example for direct .ptcss import */
/* Error: File 'footer' not found in static/. */ /* Example for direct import without specified file-type */
@import url("static/css/header.css"); /* Example for vanilla css import support */


/* Base styles */
font-size: 16px;
font-family: "Roboto", sans-serif;
color: #333;


/* List below */



.example {
    width: 25%;
    width: 50%;
    width: 75%;
    width: 100%;
    width: /* Error: Invalid list item 'list@widths[4]' */; /* Example for error */
    width: 100%; /* Example for predefined shorthand */
}

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

/* Predefined shorthands */
.main-container {
    width: 100%;
    padding: 20px;
    display: flex;
    justify-content: space-between;
}

/* Layout */
.container {
    width: 25%; /* Example for list access usage */
    text-decoration: none;
    color: var(--blue); /* Example for variable usage */
}



.header {
    width: 100%;
    color: white;
    border-radius: 10px;
    background-color: #f5f5f5;
    text-decoration: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```
This example showcases the ability of the ProtoCSS Preprocessor to handle imports, variables, shorthand properties, lists and a for loop.

## Import Functionality
The ProtoCSS preprocessor offers a powerful import feature. This functionality allows you to include various ProtoCSS files within other ProtoCSS files. By enabling the reuse of CSS rules across multiple files, this feature promotes modular design, cleaner code, and enhanced maintainability.

### Syntax
The syntax for the import feature is straightforward and intuitive. To import a file, simply use the following command:

``` css
import "filename";
```
Replace "filename" with the name of your ProtoCSS file or the URL of the file you wish to import. If the file is a standard CSS file, ensure to include the .css extension. In the absence of an explicit file extension, ProtoCSS will infer the file as a ProtoCSS file with a .ptcss extension.

### Imported Elements
The ProtoCSS Preprocessor allows the import of three main elements: 
* Variables.
* Lists.
* Mixins.

Each of these elements provides unique capabilities that can significantly improve your workflow. The following sections will provide a detailed overview of each of these elements.


## Supported Properties
The ProtoCSS Preprocessor is designed to offer a comprehensive set of shorthand properties and CSS attributes, making it easier for developers to efficiently create and maintain styles. By providing a robust set of features, ProtoCSS allows you to focus on creating visually stunning and highly functional designs with greater ease and simplicity.

List of supported properties can be found [here](https://github.com/Dcohen52/ProtoCSS/blob/main/SHORTHANDS_TABLE.md).

## Property-Declaration Shorthands
Property-declaration shorthands are a set of convenient shorthand notations for commonly used CSS properties. They allow you to quickly and easily apply styling to elements without having to remember or type out the full CSS property names and values.

Usage
To apply a property-declaration shorthand, you simply need to include the corresponding shorthand notation in your CSS code. Here's an example:

``` css
.selector {
  @w50;       /* Applies a width of 50% */
  @h100;      /* Applies a height of 100% */
  @fs20;      /* Applies a font-size of 20px */
  @c000;      /* Applies a color of #000 */
  @bds;       /* Applies a border of 1px solid */
  @br10;      /* Applies a border-radius of 10px */
  @p10;       /* Applies a padding of 10px */
  @m20;       /* Applies a margin of 20px */
  @df;        /* Applies a display of flex */
  @jcfs;      /* Applies justify-content: flex-start */
  @aic;       /* Applies align-items: center */
}
```

List of supported property-declaration shorthands can be found [here](https://github.com/Dcohen52/ProtoCSS/blob/main/PD_SHORTHANDS_TABLE.md).


## Lists
In ProtoCSS, lists are a way to mixin data that belongs together. They can be used to store a set of values, such as colors, font stacks, or breakpoints.

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


