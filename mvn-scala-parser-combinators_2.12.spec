#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-scala-parser-combinators_2.12
Version  : 1
Release  : 3
URL      : https://repo.maven.apache.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.jar
Source0  : https://repo.maven.apache.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.jar
Source1  : https://repo.maven.apache.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.jar
Source2  : https://repo.maven.apache.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.pom
Source3  : https://repo.maven.apache.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-scala-parser-combinators_2.12-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-scala-parser-combinators_2.12 package.
Group: Data

%description data
data components for the mvn-scala-parser-combinators_2.12 package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.jar
/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.0.4/scala-parser-combinators_2.12-1.0.4.pom
/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.jar
/usr/share/java/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.12/1.1.0/scala-parser-combinators_2.12-1.1.0.pom
