Summary:	A tiling tabbed X11 window manager
Summary(pl):	Zarz±dca okien dla X11
Name:		ion3
Version:	20060524
Release:	1
License:	LGPL
Group:		X11/Window Managers
#Source0Download: http://modeemi.fi/~tuomov/ion/download.html
Source0:	http://iki.fi/tuomov/dl/ion-3ds-%{version}.tar.gz
# Source0-md5:	f9dbab5a5150c9944d7c6ed9e24daef6
Source1:	ion.desktop
Source2:	ion-xsession.desktop
URL:		http://iki.fi/tuomov/ion/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1.4.3
BuildRequires:	lua51 
BuildRequires:	lua51-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Ion is a keyboard-friendly X11 window manager. It is fast and takes up
little resources.

%description -l pl
Ion jest zarz±dc± okien, obs³ugiwanym prawie wy³±cznie z klawiatury.
Jest szybki i zajmuje ma³o zasobów.

%prep
%setup -q -n ion-3ds-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--disable-static \
	--with-lua-suffix=51 \
	--with-lua-includes=%{_includedir}/lua51
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	MODULEDIR=$RPM_BUILD_ROOT%{_libdir}/ion \
	SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/ion \
	LCDIR=$RPM_BUILD_ROOT%{_libdir}/ion/lc \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ion \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	EXTRABINDIR=$RPM_BUILD_ROOT%{_libdir}/ion \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%dir %{_sysconfdir}/ion
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ion/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ion
%attr(755,root,root) %{_libdir}/ion/*.so
%attr(755,root,root) %{_libdir}/ion/ion-statusd
# used (lt_dlopen)
#%{_libdir}/ion/*.la
%attr(755,root,root) %{_libdir}/ion/ion-completefile
%{_libdir}/ion/lc
%dir %{_datadir}/ion
#%{_datadir}/ion/delib.lc
#%{_datadir}/ion/*.lua
%attr(755,root,root) %{_datadir}/ion/ion-*
#%{_datadir}/ion/welcome_message.txt
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/ion.desktop
%{_mandir}/man1/*
