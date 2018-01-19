# TODO
# -	python2 requires pathlib
#
# Conditional build:
%bcond_without	doc	# Sphinx HTML documentation
%bcond_with	tests	# unit tests
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module	eyeD3
Summary:	Python 2 module for manipulating ID3 informational tags on MP3 audio files
Summary(pl.UTF-8):	Moduł Pythona 2 służący do operacji na znacznikach ID3 plików MP3
Name:		python-%{module}
Version:	0.8
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	http://eyed3.nicfit.net/releases/%{module}-%{version}.tar.gz
# Source0-md5:	840626686e6b1bc6afca9eab99a0873a
URL:		http://eyed3.nicfit.net/
%if %{with tests} && %(locale -a | grep -q '^C\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-factory-boy >= 2.8.1
BuildRequires:	python-nose >= 1.3.7
BuildRequires:	python-pytest >= 3.0.7
BuildRequires:	python-pytest-cov >= 2.5.1
BuildRequires:	python-pytest-runner >= 2.11.1
BuildRequires:	python-six >= 1.10.0
%endif
%endif
%if %{with python2}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
%if %{with tests}
BuildRequires:	python3-factory-boy >= 2.8.1
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-pytest >= 3.0.7
BuildRequires:	python3-pytest-cov >= 2.5.1
BuildRequires:	python3-pytest-runner >= 2.11.1
BuildRequires:	python3-six >= 1.10.0
%endif
%endif
BuildRequires:	rpm-pythonprov
%if %{with doc}
BuildRequires:	python3-sphinx_issues
BuildRequires:	python3-sphinxcontrib-bitbucket
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-six >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eyeD3 is a Python module and program for processing ID3 tags.
Information about MP3 files (i.e bit rate, sample frequency, play
time, etc.) is also provided. The formats supported are ID3 v1.0/v1.1
and v2.3/v2.4.

%description -l pl.UTF-8
eyeD3 to moduł języka Python oraz wykorzystujący go program,
przetwarzający znaczniki ID3. Dostarczana jest także informacja o
samych plikach MP3 (długość, częstotliwość próbkowania itp.).
Obsługiwane są znaczniki ID3 w wersjach v1.0/v1.1 i v2.3/v2.4.

%package -n python3-%{module}
Summary:	Python 3 module for manipulating ID3 informational tags on MP3 audio files
Summary(pl.UTF-8):	Moduł Pythona 3 służący do operacji na znacznikach ID3 plików MP3
Group:		Development/Languages/Python
Requires:	python3-grako
Requires:	python3-modules >= 1:3.3
Requires:	python3-six >= 1.10.0

%description -n python3-%{module}
eyeD3 is a Python module and program for processing ID3 tags.
Information about MP3 files (i.e bit rate, sample frequency, play
time, etc.) is also provided. The formats supported are ID3 v1.0/v1.1
and v2.3/v2.4.

%description -n python3-%{module} -l pl.UTF-8
eyeD3 to moduł języka Python oraz wykorzystujący go program,
przetwarzający znaczniki ID3. Dostarczana jest także informacja o
samych plikach MP3 (długość, częstotliwość próbkowania itp.).
Obsługiwane są znaczniki ID3 w wersjach v1.0/v1.1 i v2.3/v2.4.

%package apidocs
Summary:	API documentation for Python eyeD3 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona eyeD3
Group:		Documentation

%description apidocs
API documentation for Python eyeD3 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona eyeD3.

%prep
%setup -q -n %{module}-%{version}

%build
export LC_ALL=C.UTF-8

%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs html \
	PYTHONPATH=$(pwd)/src
%endif

%install
rm -rf $RPM_BUILD_ROOT

export LC_ALL=C.UTF-8

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/eyeD3{,-py3}
%{!?with_python2:ln -sf eyeD3-py2 $RPM_BUILD_ROOT%{_bindir}/eyeD3}
%endif

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/eyeD3{,-py2}
ln -sf eyeD3-py2 $RPM_BUILD_ROOT%{_bindir}/eyeD3
%endif

# missing from py install
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p docs/eyeD3.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst README.rst
%attr(755,root,root) %{_bindir}/eyeD3-py2
%attr(755,root,root) %{_bindir}/eyeD3
%{py_sitescriptdir}/eyed3
%{py_sitescriptdir}/eyeD3-%{version}-py*.egg-info
%{_mandir}/man1/eyeD3.1*
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst README.rst
%attr(755,root,root) %{_bindir}/eyeD3-py3
%{py3_sitescriptdir}/eyed3
%{py3_sitescriptdir}/eyeD3-%{version}-py*.egg-info
%if %{without python2}
%attr(755,root,root) %{_bindir}/eyeD3
%{_mandir}/man1/eyeD3.1*
%endif
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,plugins,*.html,*.js}
%endif
