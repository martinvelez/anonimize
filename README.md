Anonimize
============

Researchers often study open source repositories or student programming projects
that may contain personally identifying information. 
Generally, we do not wish to know or compromise the privacy of individuals so we
would rather have projects that are anonimized.
This tools attempts to anonimize projects.

It does so by reducing projects to the minimal content needed to properly
compile or interpret a programming project.
Sometimes, we study thousands of projects so this anonimization also has the
side benefit of using less disk space.

This is an outline of Our method:
* Remove comments from all source code files.
* Remove any file not needed for compilation.

## Installation

    pip install anonimize

## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

* Martin Velez
* Sahana Mundewadi
* Andrew Mendoza

## License

The MIT License (MIT)

Copyright (c) 2016 Martin Velez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
