Tech. doc. of the `@-bout` specs of `src2prod`
==============================================

> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


XXXXXX ?
------------------------------

AAAAA


#### YYYYY

The first step in creating a new flavour, which we will call `myflavour`, is to use the following structure.

~~~
+ about-spec
    * EN.yaml
    * ...
~~~


`# ...` is a comment

`#: SPEC_ID in: [project, monorepo]`

`#: if: SPEC_ID == monorepo`

`#: else:`

~~~yaml
key:
  subkey_1 : TO BE TRANSLATED
  subkey_2*: TO BE TRANSLATED
  subkey_3 :
    - TO BE TRANSLATED
    - ...
  subkey_4 : |
             TO BE TRANSLATED ON SEVERAL LINES
  subkey_5:
    subsubkey_5_1: TO BE TRANSLATED
~~~

~~~yaml
author* : TO BE TRANSLATED ,
          ... ,
          TO BE TRANSLATED
          [auth_email_1@auth_provider.abc , ...]

institute* : TO BE TRANSLATED ,
             TO BE TRANSLATED
             [inst_email_1@inst_provider.abc , ...]
~~~

#### The translations, and their status

<!-- LIST OF TRANSLATIONS AND THEIR STATUS - AUTO - START -->

  * `EN` **[ok]**

<!-- LIST OF TRANSLATIONS AND THEIR STATUS - AUTO - END -->


#### Statuses with their relevant translations

<!-- LIST OF STATUSES WITH THE RELEVANT TRANSLATIONS - AUTO - START -->

  * Status **''ok''**
    + `EN`

<!-- LIST OF STATUSES WITH THE RELEVANT TRANSLATIONS - AUTO - END -->
