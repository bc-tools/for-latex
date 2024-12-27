Contribute to the `API` of `TeXfacto`
=====================================

The tanslations must be done inside folders like the `en` one above corresponding to the English version.

<!-- FOLDER STRUCT. AUTO - START -->

~~~
+ en
    + api
        + specs
~~~

<!-- FOLDER STRUCT. AUTO - END -->


> [!NOTE]
> The English and French versions are maintained by the author of `TeXfacto` in the  `en` and `fr` folders.
> You must respect their structure.

> [!CAUTION]
> Although we're going to explain how to translate the documentation, it doesn't seem relevant to do so, as English should suffice these days.
> The existence of a French version is simply a consequence of the native language of the author of `TeXfacto`.


The `changes` folder
--------------------

This folder is a communication tool where important changes are indicated without dwelling on minor modifications specific to one or more translations.


The `status` folder
-------------------

This folder is used to keep track of translations from the project's point of view. Everything is done via well-commented `YAML` files, readable by a non-coder.


New translations
----------------

> [!IMPORTANT]
> The `api` folder contains translations relating to the functionalities of `TeXfacto`.
> For each file, just focus on the text content and do not change the structure of this files.


> [!NOTE]
> The `doc` folder is reserved for documentation.
> It contains `tns.txt` files that are easy to understand.


> [!WARNING]
> Only start from one of the `fr` and `en` folders, as these are the responsibility of the `TeXfacto` author.


***Let's say you want to add support for Italian from files written in English (as mentioned above, there is no real need for the `doc` folder).***


### Method 1 : use of `git`.

  1) Recover the entire project folder via [the development branch](https://github.com/bc-tools/for-latex/tree/texfacto/TeXfacto).
  Do not use the `main` branch, which is used to freeze the latest stable versions of projects in the [for-latex](https://github.com/bc-tools/for-latex) mono repository.

  1) In the `TeXfacto/contrib/translate` folder, create an `it` copy of the `en` folder, with the short name of the language documented in [the page "IIETF language tag"](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags) from `Wikipedia`.

  1) Once the translation is complete in the `it` folder, share it via [the development branch](https://github.com/bc-tools/for-latex/tree/texfacto/TeXfacto) using a classic `git push`.


### Method 2 : communicate by e-mail.

  1) By e-mail with the email subject *"en FOR italian"*, request a version of the English translations (note the use of the English name for the new language).
  Be sure to respect the subject of the email, as the author of `TeXfacto` automates the pre-processing of this type of email.

  1) You will receive a folder named `italian` containing the English version of the latest translations.
  This folder will be the place for your contribution.

  1) Once the translation is complete, you will need to compress your `italian` file in `zip` or `rar` format before sending it by email with the email subject *"italian"*.
