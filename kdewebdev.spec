%define		_state		unstable
%define		_ver		3.3.0
%define		_snap		rc2

%define         _minlibsevr     9:3.3.0
%define         _minbaseevr     9:3.3.0
Summary:	Web development tools for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzia do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Name:		kdewebdev
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_ver}-%{_snap}.tar.bz2
# Source0-md5:	c263f04ad7bdc0252b64f7bf155bca6b
Patch0:		%{name}-quanta.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	kdesdk-cervisia
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
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.90

%description kfilereplace
TODO.

%description kfilereplace -l pl
TODO.

%package kimagemapeditor
Summary:	TODO
Summary(pl):	TODO
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools

%description kimagemapeditor
TODO.

%description kimagemapeditor -l pl
TODO.

%package klinkstatus
Summary:	TODO
Summary(pl):	TODO
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools
Conflicts:	kdewebdev-quanta_be

%description klinkstatus
TODO.

%description klinkstatus -l pl
TODO.

%package kommander
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

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
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

%description kxsldbg
TODO.

%description kxsldbg -l pl
TODO.

%package quanta
Summary:	Web development tool for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzie do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Obsoletes:	kdewebdev-quanta_be
Obsoletes:	quanta
Obsoletes:	quanta-doc

%description quanta
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description quanta -l es
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description quanta -l pl
Quanta Plus to narzêdzie do tworzenia WWW dla ¶rodowiska KDE. S³u¿y do
szybkiego tworzenia stron i staje siê dojrza³ym edytorem z wieloma
przydatnymi mo¿liwo¶ciami.

%description quanta -l pt_BR
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%prep
%setup -q -D
%patch0 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	quanta/src/quanta.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	quanta/src/quanta_be.desktop

%build
cp -f /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake 

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/{Development/*,Editors/*,Utilities/*} \
	$RPM_BUILD_ROOT%{_desktopdir}/kde
echo "Categories=Qt;KDE;Development;WebDevelopment;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/kde/kxsldbg.desktop
echo "Categories=Qt;KDE;Development;WebDevelopment;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/kde/kimagemapeditor.desktop
echo "Categories=Qt;KDE;Development;WebDevelopment;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/kde/klinkstatus.desktop
echo "Categories=Qt;KDE;Utility;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/kde/kfilereplacepart.desktop
%find_lang klinkstatus	--with-kde
%find_lang kxsldbg	--with-kde
%find_lang quanta	--with-kde
%find_lang kommander	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kommander	-p /sbin/ldconfig
%postun	kommander	-p /sbin/ldconfig

%files kfilereplace
%defattr(644,root,root,755)
%{_libdir}/kde3/libkfilereplacepart.la
%attr(755,root,root) %{_libdir}/kde3/libkfilereplacepart.so
%{_desktopdir}/kde/kfilereplacepart.desktop
%{_datadir}/apps/kfilereplacepart
%{_datadir}/services/kfilereplacepart.desktop
%{_iconsdir}/[!l]*/*/apps/kfilereplace.png

%files kimagemapeditor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimagemapeditor
%{_libdir}/kde3/libkimagemapeditor.la
%attr(755,root,root) %{_libdir}/kde3/libkimagemapeditor.so
%{_datadir}/apps/kimagemapeditor
%{_datadir}/services/kimagemapeditorpart.desktop
%{_desktopdir}/kde/kimagemapeditor.desktop
%{_iconsdir}/[!l]*/*/apps/kimagemapeditor.png

%files klinkstatus -f klinkstatus.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klinkstatus
%{_libdir}/kde3/libklinkstatuspart.la
%attr(755,root,root) %{_libdir}/kde3/libklinkstatuspart.so
%{_datadir}/apps/klinkstatuspart/pics/304.png
%{_datadir}/apps/klinkstatus/klinkstatus_shell.rc
%{_datadir}/apps/klinkstatuspart/klinkstatus_part.rc
%{_datadir}/config.kcfg/klinkstatus.kcfg
%{_datadir}/services/klinkstatus_part.desktop
%{_desktopdir}/kde/klinkstatus.desktop
%{_iconsdir}/hicolor/*/apps/klinkstatus.png

%files kommander -f kommander.lang
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
%{_datadir}/applnk/.hidden/kmdr-executor.desktop
%{_datadir}/mimelnk/application/x-kommander.desktop
%{_desktopdir}/kde/kmdr-editor.desktop
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
%attr(755,root,root) %{_bindir}/xsldbg
%{_libdir}/kde3/libkxsldbgpart.la
%attr(755,root,root) %{_libdir}/kde3/libkxsldbgpart.so
%{_datadir}/apps/kxsldbg
%{_datadir}/apps/kxsldbgpart
%{_datadir}/services/kxsldbg_part.desktop
%{_desktopdir}/kde/kxsldbg.desktop
%{_iconsdir}/[!l]*/*/actions/xsldbg_*.png
%{_mandir}/man1/kxsldbg.1*

%files quanta -f quanta.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quanta
%{_libdir}/kde3/quantadebuggergubed.la
%attr(755,root,root) %{_libdir}/kde3/quantadebuggergubed.so
#%{_datadir}/apps/kafkapart
%{_datadir}/apps/quanta
%{_datadir}/apps/templates
%{_datadir}/mimelnk/application/x-webprj.desktop
%{_datadir}/services/quanta_preview_config.desktop
%{_datadir}/services/quantadebuggergubed.desktop
%{_datadir}/servicetypes/quantadebugger.desktop
%{_desktopdir}/kde/quanta.desktop
%{_iconsdir}/[!l]*/*/apps/quanta.png
%{_iconsdir}/[!l]*/*/actions/[!x]*.png
%{_mandir}/man1/quanta.1*
