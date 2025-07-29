#
# Conditional build:
%bcond_without	guile	# disable guile support
%bcond_without	perl	# disable perl support
%bcond_without	php	# disable php support
%bcond_without	python2	# disable python 2.x support
%bcond_without	python3	# disable python 3.x support
%bcond_without	ruby	# disable ruby support
%bcond_without	tcl	# disable tcl support
#
%if "%{?php_suffix}" == ""
%define		php_suffix	83
%endif
%define		php_name	php%{?php_suffix}
Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl.UTF-8):	Generator interfejsów do Perla, Tcl-a, Guile'a i Pythona
Summary(pt_BR.UTF-8):	Gerador de Interfaces e "Wrappers" Simplificado (SWIG)
Name:		swig
Version:	4.3.1
Release:	1
License:	GPL v3+ (utility), free (library)
Group:		Development/Languages
Source0:	https://downloads.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	4929864e1b040a51370160d17669d6f1
Patch0:		%{name}-php-freearg.patch
URL:		https://swig.org/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.7.2
%{?with_guile:BuildRequires:	guile-devel >= 5:1.8}
BuildRequires:	libstdc++-devel
# used only in examples, doesn't affect actual swig build
#BuildRequires:	ocaml
# used only in examples, doesn't affect actual swig build
#BuildRequires:	octave-devel
BuildRequires:	pcre2-8-devel
%{?with_perl:BuildRequires:	perl-devel >= 1:5.8.0}
%{?with_php:BuildRequires:	%{php_name}-cli >= 8}
%{?with_php:BuildRequires:	%{php_name}-devel >= 8}
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-modules
%endif
%if %{with python2}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
%if %{with ruby}
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.6.3
%endif
%{?with_tcl:BuildRequires:	tcl-devel >= 8.3.3}
Obsoletes:	swig-ocaml < 3.0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python. In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language. However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

SWIG is entirely the product of users who have used the system and
suggested new idea. There are far too many people to thank
individually, but without this support, SWIG would be not be nearly as
powerful or fun to use as it is now. Many thanks!

%description -l pl.UTF-8
SWIG jesk kompilatorem, który próbuje ułatwić integrowanie kodu
napisanego w C, C++ lub Objective-C z językami skryptowymi, takimi jak
Perl, Tcl i Python. Mówiąc najprościej, jeśli dostarczysz mu zestaw
zadeklarowanych w ANSI C/C++ funkcji, SWIG wygeneruje Ci interfejs
pomiędzy C a Twoim ulubionym językiem skryptowym. To tylko drobna
część tego co SWIG potrafi robić, bardziej zaawansowane zastosowania
to automatyczne generowanie dokumentacji, zarządzanie bibliotekami i
modułami i wiele innych.

SWIG jest w całości dziełem ludzi, którzy go używali i wprowadzali
nowe pomysły. Zbyt wielu ich jest, aby dziękować każdemu z nich
osobno, ale bez ich wsparcia SWIG nie byłby ani tak potężnym
narzędziem, ani tak fajnym w użyciu jak jest teraz. Wiekie dzięki!

%description -l pt_BR.UTF-8
O SWIG gera interfaces para perl, python e Tcl a partir de uma arquivo
com uma interface de descrição que consiste de uma combinação de C/C++
e diretivas especiais. Permite que linguagens tipo script usem C/C++
com um mínimo de esforço.

%package guile
Summary:	SWIG module to generate Guile bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań Guile
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description guile
SWIG module to generate Guile bindings.

%description guile -l pl.UTF-8
Moduł SWIG do generowania wiązań Guile.

%package perl
Summary:	SWIG module to generate Perl bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań Perla
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
SWIG module to generate Perl bindings. It supports Perl 5.

%description perl -l pl.UTF-8
Moduł SWIG do generowania wiązań Perla. Obsługuje Perla 5.

%package php
Summary:	SWIG module to generate PHP bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań PHP
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description php
SWIG module to generate PHP bindings. It supports PHP 8.

%description php -l pl.UTF-8
Moduł SWIG do generowania wiązań PHP. Obsługuje PHP 8.

%package python
Summary:	SWIG module to generate Python bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań Pythona
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
SWIG module to generate Python bindings. It supports Python 2.7 and
3.3+

%description python -l pl.UTF-8
Moduł SWIG do generowania wiązań Pythona. Obsługuje Pythona 2.7 i
3.3+.

%package ruby
Summary:	SWIG module to generate Ruby bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań języka Ruby
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description ruby
SWIG module to generate Ruby bindings.

%description ruby -l pl.UTF-8
Moduł SWIG do generowania wiązań języka Ruby.

%package tcl
Summary:	SWIG module to generate Tcl bindings
Summary(pl.UTF-8):	Moduł SWIG do generowania wiązań języka Tcl
License:	free
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
SWIG module to generate Tcl bindings.

%description tcl -l pl.UTF-8
Moduł SWIG do generowania wiązań języka Tcl.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal} -I Tools/config
%{__autoconf}
%{__automake}
%configure \
	%{!?with_python2:--without-python} \
	%{!?with_python3:--without-python3}

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	M4_INSTALL_DIR=$RPM_BUILD_ROOT%{_aclocaldir}

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES CHANGES.current COPYRIGHT LICENSE LICENSE-UNIVERSITIES README RELEASENOTES TODO Doc
%attr(755,root,root) %{_bindir}/ccache-swig
%attr(755,root,root) %{_bindir}/swig
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/*.i
%{_datadir}/%{name}/%{version}/allkw.swg
%{_datadir}/%{name}/%{version}/director_common.swg
%{_datadir}/%{name}/%{version}/director_guard.swg
%{_datadir}/%{name}/%{version}/runtime.swg
%{_datadir}/%{name}/%{version}/swig*.swg
%{_datadir}/%{name}/%{version}/unique_ptr.swg
%{_datadir}/%{name}/%{version}/c
%{_datadir}/%{name}/%{version}/csharp
%{_datadir}/%{name}/%{version}/d
%{_datadir}/%{name}/%{version}/go
%{_datadir}/%{name}/%{version}/java
%dir %{_datadir}/%{name}/%{version}/javascript
%{_datadir}/%{name}/%{version}/javascript/javascriptkw.swg
%{_datadir}/%{name}/%{version}/javascript/jsc
%{_datadir}/%{name}/%{version}/javascript/napi
%{_datadir}/%{name}/%{version}/javascript/v8
%{_datadir}/%{name}/%{version}/lua
%{_datadir}/%{name}/%{version}/mzscheme
%{_datadir}/%{name}/%{version}/ocaml
%{_datadir}/%{name}/%{version}/octave
%{_datadir}/%{name}/%{version}/r
%{_datadir}/%{name}/%{version}/scilab
%{_datadir}/%{name}/%{version}/std
%{_datadir}/%{name}/%{version}/typemaps
%{_datadir}/%{name}/%{version}/xml
%{_examplesdir}/%{name}-%{version}

%if %{with guile}
%files guile
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/guile
%endif

%if %{with perl}
%files perl
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/perl5
%endif

%if %{with php}
%files php
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/php
%endif

%if %{with python2} || %{with python3}
%files python
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/python
%endif

%if %{with ruby}
%files ruby
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/ruby
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/tcl
%endif
