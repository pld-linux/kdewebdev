
%define		_state		snapshots
%define		_ver		3.3
%define		_snap		040513
%define		_packager	adgor

Summary:	Web development tools for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzia do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Name:		kdewebdev
Version:	%{_ver}
Release:	0.%{_snap}.0.1
Epoch:		1
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	77f2e92edd4caf70703b7274a461ef42
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel >= 9:3.2.90
BuildRequires:	libxslt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
BuildConflicts:	quanta
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description -l es
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description -l pl
Quanta Plus to narzêdzie do tworzenia WWW dla ¶rodowiska KDE. S³u¿y do
szybkiego tworzenia stron i staje siê dojrza³ym edytorem z wieloma
przydatnymi mo¿liwo¶ciami.

%description -l pt_BR
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%package kfilereplace
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kfilereplace
TODO.

%description kfilereplace -l pl
TODO.

%package kimagemapeditor
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kimagemapeditor
TODO.

%description kimagemapeditor -l pl
TODO.

%package kommander
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kommander
TODO.

%description kommander -l pl
TODO.

%package kommander-devel
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Libraries
Requires:	%{name}-kommander = %{epoch}:%{version}-%{release}

%description kommander-devel
TODO.

%description kommander-devel -l pl
TODO.

%package kxsldbg
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kxsldbg
TODO.

%description kxsldbg -l pl
TODO.

%package quanta_be
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	quanta
Obsoletes:	quanta-doc

%description quanta_be
TODO.

%description quanta_be -l pl
TODO.

%prep
%setup -q -n %{name}-%{_snap}

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake 
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
#	--enable-final \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/{.hidden/*,Development/*,Editors/*,Utilities/*} \
	$RPM_BUILD_ROOT%{_desktopdir}/kde
echo "Categories=Qt;KDE;Development;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kxsldbg.desktop
echo -e "\\nCategories=Qt;KDE;Development;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kimagemapeditor.desktop

%find_lang kxsldbg --with-kde
%find_lang quanta_be --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kommander	-p /sbin/ldconfig
%postun	kommander	-p /sbin/ldconfig

%files kfilereplace
%defattr(644,root,root,755)
%{_libdir}/kde3/libkfilereplacepart.la
%attr(755,root,root) %{_libdir}/kde3/libkfilereplacepart.so
%{_datadir}/apps/kfilereplacepart
%{_datadir}/services/kfilereplacepart.desktop
%{_iconsdir}/[!l]*/*/apps/kfilereplace.png

%files kimagemapeditor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimagemapeditor
%{_libdir}/kde3/libkimagemapeditor.la
%attr(755,root,root) %{_libdir}/kde3/libkimagemapeditor.so
%{_datadir}/apps/kimagemapeditor
%{_desktopdir}/kde/kimagemapeditor.desktop
%{_iconsdir}/[!l]*/*/apps/kimagemapeditor.png

%files kommander
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmdr-editor
%attr(755,root,root) %{_bindir}/kmdr-executor
%attr(755,root,root) %{_bindir}/kmdr-plugins
%{_libdir}/libkommanderplugin.la
%attr(755,root,root) %{_libdir}/libkommanderplugin.so.*.*.*
%{_libdir}/libkommanderwidget.la
%attr(755,root,root) %{_libdir}/libkommanderwidget.so.*.*.*
%{_libdir}/libkommanderwidgets.la
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so.*.*.*
%{_datadir}/mimelnk/application/x-kommander.desktop
%{_desktopdir}/kde/kmdr-editor.desktop
%{_desktopdir}/kde/kmdr-executor.desktop
%{_mandir}/man1/kmdr-editor.1*
%{_mandir}/man1/kmdr-executor.1*

%files kommander-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkommanderplugin.so
%attr(755,root,root) %{_libdir}/libkommanderwidget.so
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so
%{_includedir}/kommanderfactory.h
%{_includedir}/kommanderplugin.h
%{_includedir}/kommanderwidget.h

%files kxsldbg -f kxsldbg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxsldbg
%{_libdir}/kde3/libkxsldbgpart.la
%attr(755,root,root) %{_libdir}/kde3/libkxsldbgpart.so
%{_datadir}/apps/kxsldbg
%{_datadir}/apps/kxsldbgpart
%{_datadir}/services/kxsldbg_part.desktop
%{_desktopdir}/kde/kxsldbg.desktop
%{_iconsdir}/[!l]*/*/actions/xsldbg_*.png
%{_mandir}/man1/kxsldbg.1*

%files quanta_be -f quanta_be.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quanta_be
%{_datadir}/apps/kafkapart
%{_datadir}/apps/quanta_be
%{_datadir}/apps/templates
%{_desktopdir}/kde/quanta_be.desktop
%{_iconsdir}/[!l]*/*/apps/quanta_be.png
%{_iconsdir}/[!l]*/*/actions/[!x]*.png
%{_mandir}/man1/quanta.1*
