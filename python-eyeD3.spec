
%define		module	eyeD3

Summary:	Module for manipulating ID3 informational tags on MP3 audio files
Summary(pl):	Modu³ s³u¿±cy do manipulacji znacznikami ID3 plików MP3
Name:		python-%{module}
Version:	0.6.3
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://eyed3.nicfit.net/releases/%{module}-%{version}.tar.gz
# Source0-md5:	40181b28bf161e0fcb11b04fecafc994
URL:		http://eyed3.nicfit.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eyeD3 is a Python module and program for processing ID3 tags.
Information about MP3 files (i.e bit rate, sample frequency, play
time, etc.) is also provided. The formats supported are ID3 v1.0/v1.1
and v2.3/v2.4.

%description -l pl
eyeD3 to modu³ jêzyka Python oraz wykorzystuj±cy go program,
przetwarzaj±cy znaczniki ID3. Dostarczana jest tak¿e informacja o
samych plikach MP3 (d³ugo¶æ, czêstotliwo¶æ próbkowania itp.).
Obs³ugiwane s± znaczniki ID3 w wersjach v1.0/v1.1 i v2.3/v2.4.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{module}
%doc README.html AUTHORS THANKS ChangeLog
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{_mandir}/man1/%{module}.1*
