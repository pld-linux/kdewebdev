%define		_state		unstable
%define		_ver		3.3.0

%define         _minlibsevr     9:3.3.0
%define         _minbaseevr     9:3.3.0
Summary:	Web development tools for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzia do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Name:		kdewebdev
Version:	%{_ver}
Release:	0.1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/3.3/src/%{name}-%{version}.tar.bz2
#Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_ver}-%{_snap}.tar.bz2
# Source0-md5:	c263f04ad7bdc0252b64f7bf155bca6b
Patch0:		%{name}-quanta.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	kdesdk-libcvsservice-devel
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
Summary:	A powerful string replacer
Summary(pl):	Rozbudowane narzêdzie do zamiany tekstu
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.90

%description kfilereplace
KFileReplace is a KDE utility which replace some strings with others
in a lot of files in an only operation.

%description kfilereplace -l pl
KFileReplace to narzêdzie do masowej zmiany ró¿nych tekstów w du¿ej
ilo¶ci plików, podczas jednej operacji.

%package kimagemapeditor
Summary:	An HTML image map editor
Summary(pl):	Edytor map obrazów w HTML
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools

%description kimagemapeditor
An HTML image map editor.

%description kimagemapeditor -l pl
Edytor map obrazów w HTML.

%package klinkstatus
Summary:	Link checker for KDE.
Summary(pl):	Program do sprawdzania odno¶ników pod KDE.
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools
Conflicts:	kdewebdev-quanta_be

%description klinkstatus
KLinkStatus is an Open Source tool for checking links in a web page.
It can search by depth, domain or both. On a domain search it's also
possible to choose the search depth of URL's with foreign domain. For
performance, it supports several simultaneous connections and try to
use the same connection for the same sequence of requests.

%description klinkstatus -l pl
KLinkStatus jest narzêdziem do sprawdzania odno¶ników na stronie.
Obs³uguje wyszukiwanie wed³ug g³êboko¶ci, domeny lub obu naraz. W
wyszukiwaniu wed³ug domeny mo¿na równie¿ dodaæ maksymaln± g³êboko¶æ
dla pozosta³ych domen. Dla uzyskania jak najlepszej wydajno¶ci program
obs³uguje symultaniczne po³±czenia oraz próbuje wykorzystaæ jedno
po³±czenie dla wszystkich sekwencji ¿±dañ.

%package kommander
Summary:	A langauage independent visual dialog building tool
Summary(pl):	Niezale¿ne od jêzyka narzêdzie do budowy okien dialogowych
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

%description kommander
Kommander is a visual dialog building tool which may be expanded to
create full mainwindow applications. The primary objective is to
create as much functionality as possible without using any scripting
language. This is provided by the following features:
- Specials - these are prefaced with an "@" like @widgetText. The
  offer special features like the value of a widget, functions, aliases,
  global variables and such.
- DCOP integration - this allows Kommander dialogs to control and be
  controled in interactions with other KDE applicatins.
- Signals and Slots - this is a little less intuitive to a new user.
  It is under review for how we process things in the first major
  release. These offer a limited event model for when a button is pushed
  or a widget is changed. Combined with "Population Text" it is rather
  powerful.

The central key feature of Kommander dialogs is that you can bind text
(Kommander Text) to a widget. So if you have @widget1 and @widget2 and
they are line edits you can set Kommander to show their contents by
entering @widgetText in their Kommander Text area. Then enter hello in
@widget1 and world in @widget2. A button can have the string My first
@widget1 @widget2 program in Kommander If you run this dialog from a
console it will output My first hello world program in Kommander

Kommander also seeks to build on standards. It is built on the Qt
Designer framework and creates *.ui files which it renames to *.kmdr.
It can easily import any KDE widget and this can be done without
having to rebuild Kommander, by using plugins.

Kommander's other significant factor is being language neutral and
allowing a Kommander dialog to be extended by using any scripting
language Kommander positions it's self in a unique position for wide
spread adoption. Multiple script languages can be used in a single
dialog and applications can be taken over by people using a different
language than the original developer and gradually converting and
extending it. New widgets and featurs can be instantly leveraged by
all available languages.

%description kommander -l pl
TODO.

%package kommander-devel
Summary:	Development files for kommander
Summary(pl):	Nag³ówki dla kommandera
Group:		X11/Development/Libraries
Requires:	%{name}-kommander = %{epoch}:%{version}-%{release}

%description kommander-devel
Development files for kommander.

%description kommander-devel -l pl
Nag³ówki dla kommandera.

%package kxsldbg
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

%description kxsldbg
KXsldbg is a graphical debugger and a frontend to xsldbg. It allows
to:
- set and modify breakpoints
- display value of expressions
- display in formation about breakpoints, templates, variables,
  callstack, stylesheets and entities found
- move around XSL source and XML document via XPaths
- lookup PUBLIC and SYSTEM ID's in the current XML catalog

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
%setup -q
%patch0 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	quanta/src/quanta.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	quanta/src/quanta_be.desktop

echo "Categories=Qt;KDE;Development;WebDevelopment;" >> ./kimagemapeditor/kimagemapeditor.desktop
echo "Categories=Qt;KDE;Development;WebDevelopment;" >> ./kxsldbg/kxsldbg.desktop
echo "Categories=Qt;KDE;Development;WebDevelopment;" >> ./klinkstatus/src/klinkstatus.desktop
echo "Categories=Qt;KDE;Utility;" >> ./kfilereplace/kfilereplacepart.desktop

%build
cp -f %{_datadir}/automake/config.sub admin

export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/{Development/*,Editors/*,Utilities/*} \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

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
