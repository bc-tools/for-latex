### Some rules for pure coding

The `STY` parts of the final product are directly inside a subfolder of the source directory. They use the following template with some magical comments.

~~~latex
% == PACKAGES == %

% ...

% == OPTIONS == %

% ...

% == TOOLS == %

% ...
~~~


Here is how to use those magic comments.

  1. Only `% == TOOLS == %` is mandatory.

  1. The order above must be respected even if you don't use all the magic comments.

  1. The comment `% == PACKAGES == %` indicates lines importing packages via `\RequirePackage` or `\usepackage`, but also via `\tcbuselibrary` for example.

  1. The comment `% == OPTIONS == %` is dedicated to the management of the package options.

  1. The comment `% == TOOLS == %` is for definitions of environments and macros, and also for settings using macros.
