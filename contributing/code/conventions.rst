.. _contribute-code-conventions:

===========
Conventions
===========

This document describes coding standards and conventions used in
the **mangos-zero** codebase to make it more consistent and predictable.

Method Names
------------

We have not yet agreed on a convention for naming functions.

.. _contributing-code-conventions-deprecations:

Deprecations
------------

From time to time, some classes and/or methods are deprecated; that happens
when a feature implementation cannot be changed because of backward
compatibility issues, but we still want to propose a "better" alternative. In
that case, the old implementation can simply be **deprecated**.

A feature is marked as deprecated by adding a ``@deprecated`` Doxygen comment
to relevant classes, methods, properties, ...::

    /**
     * @deprecated Deprecated since version 1.X, to be removed in 2.Y. Use XXX instead.
     */

The deprecation message should indicate the version when the class/method was
deprecated, the version when it will be removed, and whenever possible, how
the feature was replaced.

A deprecation error must also be triggered to help people with the migration
starting one or two minor versions before the version where the feature will be
removed (depending on the criticality of the removal)::

    DEBUG_LOG("XXX() is deprecated and will be removed in 2.Y. Use XXX instead.");
