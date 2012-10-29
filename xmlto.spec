%include	/usr/lib/rpm/macros.perl

Summary:	A tool for converting XML files to various formats
Name:		xmlto
Version:	0.0.25
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
# Source0-md5:	6b6267b1470f8571fe5f63a128970364
URL:		http://cyberelk.net/tim/xmlto/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt-progs
BuildRequires:	rpm-perlprov
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package for converting XML files to various formats using
XSL stylesheets.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
