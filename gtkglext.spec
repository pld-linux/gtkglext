Summary:	OpenGL extension to GTK
Summary(pl):	Rozszerzenie OpenGL dla GTK
Name:		gtkglext
Version:	1.0.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	b8743a53a4062f3bf03062bafa25e924
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.1.2
BuildRequires:	libtool >= 1:1.4.2-9
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK,
and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.

As opposed to Janne Loff's GtkGLArea, it does not provide any OpenGL
widget, but an interface to use OpenGL on *ANY* GTK+ widget. 

%description -l pl
GtkGLExt udost�pnia obiekty GDK obs�uguj�ce rysowanie OpenGL w GTK
oraz dodatki do API GtkWidget dodaj�ce obs�ug� OpenGL do widget�w
GTK+.

W przeciwie�stwie do GtkGLArea Janne Loffa, nie udost�pnia widgetu
OpenGL, ale interfejs do u�ywania OpenGL w *KA�DYM* widgecie GTK+.

%package devel
Summary:	Development files for GtkGLExt
Summary(pl):	Pliki programistyczne GtkGLExt
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+2-devel => 2.1.2

%description devel
Development files for GtkGLExt.

%description devel -l pl
Pliki programistyczne GtkGLExt.

%package static
Summary:	GtkGLExt static libraries
Summary(pl):	Statyczne biblioteki GtkGLExt
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLExt static libraries.

%description static -l pl
Statyczne biblioteki GtkGLExt.

%prep
%setup -q

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--with-html-path=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	HTML_DIR=%{_gtkdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/%{name}*
%{_includedir}/%{name}*
%{_pkgconfigdir}/*
%{_aclocaldir}/*.m4
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
