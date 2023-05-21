# ProtoCSS CLI Documentation

The ProtoCSS CLI is a command-line interface that provides a convenient way to interact with ProtoCSS and perform various operations. This section provides an overview of the functionality offered by the ProtoCSS CLI.

## General Commands

- `docs`: Displays the documentation for the ProtoCSS CLI.
- `exit`, `quit`, `close`: Closes the CLI and exits the program.
- `convert`: Converts a ProtoCSS file to CSS.
- `version`: Displays the current version of ProtoCSS.
- `help`: Displays the general documentation and supported commands.

## Conversion Commands

The ProtoCSS CLI allows you to convert ProtoCSS files to CSS using different options.

### Convert a Single File

To convert a single ProtoCSS file to CSS, use the following command:

```commandline
convert -f <file-path> -o <output-path>
```


- `<file-path>`: The path to the ProtoCSS file.
- `<output-path>` (optional): The path to the directory where the converted CSS file should be saved. If not provided, the CSS file will be saved in the same directory as the ProtoCSS file.

### Convert Multiple Files

To convert multiple ProtoCSS files to CSS, use the following command:

```commandline
convert -mf <file-path> -o <output-path>
```


- `<file-path1> <file-path2> ... <file-pathN>`: The paths to the ProtoCSS files to be converted.
- `<output-path>` (optional): The path to the directory where the converted CSS files should be saved. If not provided, the CSS files will be saved in the same directory as the corresponding ProtoCSS files.

### Convert Files in a Directory

To convert all ProtoCSS files in a directory to CSS, use the following command:

```commandline
convert -d <directory-path> -o <output-path>
```

- `<directory-path>`: The path to the directory containing the ProtoCSS files.
- `<output-path>` (optional): The path to the directory where the converted CSS files should be saved. If not provided, the CSS files will be saved in the same directory as the corresponding ProtoCSS files.

### Convert with Default Options

The ProtoCSS CLI also provides default conversion options for convenience.

#### Convert a Single File (Default)

To convert a single ProtoCSS file to CSS with default options, use the following command:
```
convert -fd <file-path1> <file-path2> ... <file-pathN>
```

- `<file-path1> <file-path2> ... <file-pathN>`: The paths to the ProtoCSS files to be converted. The CSS files will be saved in the same directory as the corresponding ProtoCSS files.

#### Convert Multiple Files (Default)

To convert multiple ProtoCSS files to CSS with default options, use the following command:
    
```commandline
convert -mfd <file-path1> <file-path2> ... <file-pathN>
```

- `<file-path1> <file-path2> ... <file-pathN>`: The paths to the ProtoCSS files to be converted. The CSS files will be saved in the same directory as the corresponding ProtoCSS files.

#### Convert Files in a Directory (Default)

To convert all ProtoCSS files in a directory to CSS with default options, use the following command:

```commandline
convert -dd <directory-path>
```

- `<directory-path>`: The path to the directory containing the ProtoCSS files. The CSS files will be saved in the same directory as the corresponding ProtoCSS files.

## Examples

Here are a few examples to demonstrate the usage of the ProtoCSS CLI:

- Convert a single ProtoCSS file to CSS:

```commandline
convert -f <file-path> -o <output-path>
```

- Convert multiple ProtoCSS files to CSS:

```commandline
convert -mf file1.ptcss file2.ptcss file3.ptcss -o output-dir
```

- Convert all ProtoCSS files in a directory to CSS:
```commandline
convert -d input-dir -o output-dir
```

- Convert a single ProtoCSS file to CSS with default options:
```commandline
convert -fd input.ptcss
```

- Convert multiple ProtoCSS files to CSS with default options:
```commandline
convert -mfd file1.ptcss file2.ptcss file3.ptcss
```

- Convert all ProtoCSS files in a directory to CSS with default options:

```commandline
convert -dd input-dir
```