.. _contribute-code-standards:

================
Coding Standards
================

When contributing code to **mangos-zero**, you must follow its coding standards.

**mangos-zero** follow a modified version of the ANSI coding standard.

Here is a short example containing most features described below:

.. code-block:: cpp

    #include <string>

    // Database exceptions
    class Exception
    {
        public:
            Exception(const std::string& message): message(message)
            { }
            virtual ~Exception()
            { }
            const std::string& getMessage() {return message;}
        private:
            std::string message;
    };

Structure
---------

* Add a single space after each comma delimiter;

* Add a single space around operators (``==``, ``&&``, ...);

* Add a comma after each array item in a multi-line array, even after the
  last one;

* Add a blank line before ``return`` statements, unless the return is alone
  inside a statement-group (like an ``if`` statement);

* Use braces to indicate control structure body regardless of the number of
  statements it contains;

* Define one class per file - this does not apply to private helper classes
  that are not intended to be instantiated from the outside;

* Declare class properties before methods;

* Declare public methods first, then protected ones and finally private ones;

* Use parentheses when instantiating classes regardless of the number of
  arguments the constructor has;

* Exception message strings should be concatenated using :c:func:`sprintf`.

Naming Conventions
------------------

* Use camelCase, not underscores, for variable, function and method
  names, arguments;

* Use underscores for option names and parameter names;

* Use namespaces for all classes;

* Prefix abstract classes with ``Abstract``.

* Suffix interfaces with ``Interface``;

* Suffix exceptions with ``Exception``;

* Use alphanumeric characters and underscores for file names;

* Don't forget to look at the more verbose :doc:`conventions` document for
  more subjective naming considerations.

Documentation
-------------

* Add Doxygen blocks for all classes, methods, and functions;

* Omit the ``\return`` tag if the method does not return anything;

License
-------

* **mangos-zero** is released under the GNU GPL version 2 license, and the
  license block has to be present at the top of every file.
