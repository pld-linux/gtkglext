Summary:	OpenGL extension to GTK
Name:		gtkglext
Version:	0.5.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
URL:		http://gtkglext.sourceforge.net/
Patch0:		%{name}-drawpixbuf.patch
Patch1:		%{name}-visual.patch
Requires:	OpenGL
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+2-devel => 2.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share

%description
GtkGLExt provides the GDK objects to support OpenGL rendering in GTK, and
GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.

As opposed to Jane Loff's GtkGLArea , it does not provide any OpenGL
widget, but an interface to use OpenGL on *ANY* GTK+ widget. 

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
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/reference/gtkglext/html/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/%{name}*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
