%define		module	eyeD3
Summary:	Module for manipulating ID3 informational tags on MP3 audio files
Summary(pl.UTF-8):	Moduł służący do manipulacji znacznikami ID3 plików MP3
Name:		python-%{module}
Version:	0.6.18
Release:	3
License:	GNU
Group:		Development/Languages/Python
Source0:	http://eyed3.nicfit.net/releases/%{module}-%{version}.tar.gz
# Source0-md5:	ad545c55bb8bdd579e8d14c5bdaacee5
URL:		http://eyed3.nicfit.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
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

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{module}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.html NEWS TODO
%attr(755,root,root) %{_bindir}/%{module}
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/eyeD3-%{version}-*.egg-info
%{_mandir}/man1/%{module}.1*
