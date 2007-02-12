Summary:	OpenGL extension to GTK
Summary(pl.UTF-8):   Rozszerzenie OpenGL dla GTK
Name:		gtkglext
Version:	1.2.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
# Source0-md5:	ed7ba24ce06a8630c07f2d0ee5f04ab4
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel >= 1:2.1.2
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK,
and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.

As opposed to Janne Loff's GtkGLArea, it does not provide any OpenGL
widget, but an interface to use OpenGL on *ANY* GTK+ widget.

%description -l pl.UTF-8
GtkGLExt udostępnia obiekty GDK obsługujące rysowanie OpenGL w GTK
oraz dodatki do API GtkWidget dodające obsługę OpenGL do widgetów
GTK+.

W przeciwieństwie do GtkGLArea Janne Loffa, nie udostępnia widgetu
OpenGL, ale interfejs do używania OpenGL w *KAŻDYM* widgecie GTK+.

%package devel
Summary:	Development files for GtkGLExt
Summary(pl.UTF-8):   Pliki programistyczne GtkGLExt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	gtk+2-devel >= 1:2.1.2
Requires:	xorg-lib-libXmu-devel

%description devel
Development files for GtkGLExt.

%description devel -l pl.UTF-8
Pliki programistyczne GtkGLExt.

%package static
Summary:	GtkGLExt static libraries
Summary(pl.UTF-8):   Statyczne biblioteki GtkGLExt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GtkGLExt static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GtkGLExt.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-gdktarget=x11

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* README TODO
%attr(755,root,root) %{_libdir}/libg[dt]kglext-x11-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg[dt]kglext-x11-*.so
%{_libdir}/libg[dt]kglext-x11-*.la
%{_libdir}/%{name}-*
%{_includedir}/%{name}-*
%{_pkgconfigdir}/g[dt]kglext-*.pc
%{_aclocaldir}/gtkglext-*.m4
%{_gtkdocdir}/gtkglext

%files static
%defattr(644,root,root,755)
%{_libdir}/libg[dt]kglext-x11-*.a
