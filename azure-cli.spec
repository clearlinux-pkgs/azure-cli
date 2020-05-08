#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cli
Version  : 2.5.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/50/89/fc648d7d528e783e8ff57a4acd833aeecf37f9a2a4a4cdf852422793b96d/azure-cli-2.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/89/fc648d7d528e783e8ff57a4acd833aeecf37f9a2a4a4cdf852422793b96d/azure-cli-2.5.1.tar.gz
Summary  : Microsoft Azure Command-Line Tools
Group    : Development/Tools
License  : MIT
Requires: azure-cli-bin = %{version}-%{release}
Requires: azure-cli-license = %{version}-%{release}
Requires: azure-cli-python = %{version}-%{release}
Requires: azure-cli-python3 = %{version}-%{release}
Requires: antlr4-python3-runtime
Requires: azure-batch
Requires: azure-cli-command-modules-nspkg
Requires: azure-cli-core
Requires: azure-cli-nspkg
Requires: azure-cli-telemetry
Requires: azure-cosmos
Requires: azure-datalake-store
Requires: azure-functions-devops-build
Requires: azure-graphrbac
Requires: azure-keyvault
Requires: azure-loganalytics
Requires: azure-mgmt-advisor
Requires: azure-mgmt-apimanagement
Requires: azure-mgmt-appconfiguration
Requires: azure-mgmt-applicationinsights
Requires: azure-mgmt-authorization
Requires: azure-mgmt-batch
Requires: azure-mgmt-batchai
Requires: azure-mgmt-billing
Requires: azure-mgmt-botservice
Requires: azure-mgmt-cdn
Requires: azure-mgmt-cognitiveservices
Requires: azure-mgmt-compute
Requires: azure-mgmt-consumption
Requires: azure-mgmt-containerinstance
Requires: azure-mgmt-containerregistry
Requires: azure-mgmt-containerservice
Requires: azure-mgmt-cosmosdb
Requires: azure-mgmt-datalake-analytics
Requires: azure-mgmt-datalake-store
Requires: azure-mgmt-datamigration
Requires: azure-mgmt-deploymentmanager
Requires: azure-mgmt-devtestlabs
Requires: azure-mgmt-dns
Requires: azure-mgmt-eventgrid
Requires: azure-mgmt-eventhub
Requires: azure-mgmt-hdinsight
Requires: azure-mgmt-imagebuilder
Requires: azure-mgmt-iotcentral
Requires: azure-mgmt-iothub
Requires: azure-mgmt-iothubprovisioningservices
Requires: azure-mgmt-keyvault
Requires: azure-mgmt-kusto
Requires: azure-mgmt-loganalytics
Requires: azure-mgmt-managedservices
Requires: azure-mgmt-managementgroups
Requires: azure-mgmt-maps
Requires: azure-mgmt-marketplaceordering
Requires: azure-mgmt-media
Requires: azure-mgmt-monitor
Requires: azure-mgmt-msi
Requires: azure-mgmt-netapp
Requires: azure-mgmt-network
Requires: azure-mgmt-policyinsights
Requires: azure-mgmt-privatedns
Requires: azure-mgmt-rdbms
Requires: azure-mgmt-recoveryservices
Requires: azure-mgmt-recoveryservicesbackup
Requires: azure-mgmt-redhatopenshift
Requires: azure-mgmt-redis
Requires: azure-mgmt-relay
Requires: azure-mgmt-reservations
Requires: azure-mgmt-resource
Requires: azure-mgmt-search
Requires: azure-mgmt-security
Requires: azure-mgmt-servicebus
Requires: azure-mgmt-servicefabric
Requires: azure-mgmt-signalr
Requires: azure-mgmt-sql
Requires: azure-mgmt-sqlvirtualmachine
Requires: azure-mgmt-storage
Requires: azure-mgmt-trafficmanager
Requires: azure-mgmt-web
Requires: azure-multiapi-storage
Requires: azure-storage-blob
Requires: colorama
Requires: cryptography
Requires: fabric
Requires: javaproperties
Requires: jsmin
Requires: jsondiff
Requires: knack
Requires: paramiko
Requires: pyOpenSSL
Requires: python-mock
Requires: pytz
Requires: requests
Requires: scp
Requires: six
Requires: sshtunnel
Requires: vsts-cd-manager
Requires: websocket_client
Requires: xmltodict
BuildRequires : antlr4-python3-runtime
BuildRequires : azure-batch
BuildRequires : azure-cli-command-modules-nspkg
BuildRequires : azure-cli-core
BuildRequires : azure-cli-nspkg
BuildRequires : azure-cli-telemetry
BuildRequires : azure-cosmos
BuildRequires : azure-datalake-store
BuildRequires : azure-functions-devops-build
BuildRequires : azure-graphrbac
BuildRequires : azure-keyvault
BuildRequires : azure-loganalytics
BuildRequires : azure-mgmt-advisor
BuildRequires : azure-mgmt-apimanagement
BuildRequires : azure-mgmt-appconfiguration
BuildRequires : azure-mgmt-applicationinsights
BuildRequires : azure-mgmt-authorization
BuildRequires : azure-mgmt-batch
BuildRequires : azure-mgmt-batchai
BuildRequires : azure-mgmt-billing
BuildRequires : azure-mgmt-botservice
BuildRequires : azure-mgmt-cdn
BuildRequires : azure-mgmt-cognitiveservices
BuildRequires : azure-mgmt-compute
BuildRequires : azure-mgmt-consumption
BuildRequires : azure-mgmt-containerinstance
BuildRequires : azure-mgmt-containerregistry
BuildRequires : azure-mgmt-containerservice
BuildRequires : azure-mgmt-cosmosdb
BuildRequires : azure-mgmt-datalake-analytics
BuildRequires : azure-mgmt-datalake-store
BuildRequires : azure-mgmt-datamigration
BuildRequires : azure-mgmt-deploymentmanager
BuildRequires : azure-mgmt-devtestlabs
BuildRequires : azure-mgmt-dns
BuildRequires : azure-mgmt-eventgrid
BuildRequires : azure-mgmt-eventhub
BuildRequires : azure-mgmt-hdinsight
BuildRequires : azure-mgmt-imagebuilder
BuildRequires : azure-mgmt-iotcentral
BuildRequires : azure-mgmt-iothub
BuildRequires : azure-mgmt-iothubprovisioningservices
BuildRequires : azure-mgmt-keyvault
BuildRequires : azure-mgmt-kusto
BuildRequires : azure-mgmt-loganalytics
BuildRequires : azure-mgmt-managedservices
BuildRequires : azure-mgmt-managementgroups
BuildRequires : azure-mgmt-maps
BuildRequires : azure-mgmt-marketplaceordering
BuildRequires : azure-mgmt-media
BuildRequires : azure-mgmt-monitor
BuildRequires : azure-mgmt-msi
BuildRequires : azure-mgmt-netapp
BuildRequires : azure-mgmt-network
BuildRequires : azure-mgmt-policyinsights
BuildRequires : azure-mgmt-privatedns
BuildRequires : azure-mgmt-rdbms
BuildRequires : azure-mgmt-recoveryservices
BuildRequires : azure-mgmt-recoveryservicesbackup
BuildRequires : azure-mgmt-redhatopenshift
BuildRequires : azure-mgmt-redis
BuildRequires : azure-mgmt-relay
BuildRequires : azure-mgmt-reservations
BuildRequires : azure-mgmt-resource
BuildRequires : azure-mgmt-search
BuildRequires : azure-mgmt-security
BuildRequires : azure-mgmt-servicebus
BuildRequires : azure-mgmt-servicefabric
BuildRequires : azure-mgmt-signalr
BuildRequires : azure-mgmt-sql
BuildRequires : azure-mgmt-sqlvirtualmachine
BuildRequires : azure-mgmt-storage
BuildRequires : azure-mgmt-trafficmanager
BuildRequires : azure-mgmt-web
BuildRequires : azure-multiapi-storage
BuildRequires : azure-storage-blob
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : cryptography
BuildRequires : fabric
BuildRequires : javaproperties
BuildRequires : jsmin
BuildRequires : jsondiff
BuildRequires : knack
BuildRequires : paramiko
BuildRequires : pyOpenSSL
BuildRequires : python-mock
BuildRequires : pytz
BuildRequires : requests
BuildRequires : scp
BuildRequires : six
BuildRequires : sshtunnel
BuildRequires : vsts-cd-manager
BuildRequires : xmltodict
Patch1: Remove-dependencies-constraints.patch

%description
===================
        
        A great cloud needs great tools; we're excited to introduce *Azure CLI*, our next generation multi-platform command line experience for Azure.
        
        Usage
        =====

%package bin
Summary: bin components for the azure-cli package.
Group: Binaries
Requires: azure-cli-license = %{version}-%{release}

%description bin
bin components for the azure-cli package.


%package license
Summary: license components for the azure-cli package.
Group: Default

%description license
license components for the azure-cli package.


%package python
Summary: python components for the azure-cli package.
Group: Default
Requires: azure-cli-python3 = %{version}-%{release}

%description python
python components for the azure-cli package.


%package python3
Summary: python3 components for the azure-cli package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cli)
Requires: pypi(antlr4_python3_runtime)
Requires: pypi(azure_batch)
Requires: pypi(azure_cli_command_modules_nspkg)
Requires: pypi(azure_cli_core)
Requires: pypi(azure_cli_nspkg)
Requires: pypi(azure_cli_telemetry)
Requires: pypi(azure_cosmos)
Requires: pypi(azure_datalake_store)
Requires: pypi(azure_functions_devops_build)
Requires: pypi(azure_graphrbac)
Requires: pypi(azure_keyvault)
Requires: pypi(azure_loganalytics)
Requires: pypi(azure_mgmt_advisor)
Requires: pypi(azure_mgmt_apimanagement)
Requires: pypi(azure_mgmt_appconfiguration)
Requires: pypi(azure_mgmt_applicationinsights)
Requires: pypi(azure_mgmt_authorization)
Requires: pypi(azure_mgmt_batch)
Requires: pypi(azure_mgmt_batchai)
Requires: pypi(azure_mgmt_billing)
Requires: pypi(azure_mgmt_botservice)
Requires: pypi(azure_mgmt_cdn)
Requires: pypi(azure_mgmt_cognitiveservices)
Requires: pypi(azure_mgmt_compute)
Requires: pypi(azure_mgmt_consumption)
Requires: pypi(azure_mgmt_containerinstance)
Requires: pypi(azure_mgmt_containerregistry)
Requires: pypi(azure_mgmt_containerservice)
Requires: pypi(azure_mgmt_cosmosdb)
Requires: pypi(azure_mgmt_datalake_analytics)
Requires: pypi(azure_mgmt_datalake_store)
Requires: pypi(azure_mgmt_datamigration)
Requires: pypi(azure_mgmt_deploymentmanager)
Requires: pypi(azure_mgmt_devtestlabs)
Requires: pypi(azure_mgmt_dns)
Requires: pypi(azure_mgmt_eventgrid)
Requires: pypi(azure_mgmt_eventhub)
Requires: pypi(azure_mgmt_hdinsight)
Requires: pypi(azure_mgmt_imagebuilder)
Requires: pypi(azure_mgmt_iotcentral)
Requires: pypi(azure_mgmt_iothub)
Requires: pypi(azure_mgmt_iothubprovisioningservices)
Requires: pypi(azure_mgmt_keyvault)
Requires: pypi(azure_mgmt_kusto)
Requires: pypi(azure_mgmt_loganalytics)
Requires: pypi(azure_mgmt_managedservices)
Requires: pypi(azure_mgmt_managementgroups)
Requires: pypi(azure_mgmt_maps)
Requires: pypi(azure_mgmt_marketplaceordering)
Requires: pypi(azure_mgmt_media)
Requires: pypi(azure_mgmt_monitor)
Requires: pypi(azure_mgmt_msi)
Requires: pypi(azure_mgmt_netapp)
Requires: pypi(azure_mgmt_network)
Requires: pypi(azure_mgmt_policyinsights)
Requires: pypi(azure_mgmt_privatedns)
Requires: pypi(azure_mgmt_rdbms)
Requires: pypi(azure_mgmt_recoveryservices)
Requires: pypi(azure_mgmt_recoveryservicesbackup)
Requires: pypi(azure_mgmt_redhatopenshift)
Requires: pypi(azure_mgmt_redis)
Requires: pypi(azure_mgmt_relay)
Requires: pypi(azure_mgmt_reservations)
Requires: pypi(azure_mgmt_resource)
Requires: pypi(azure_mgmt_search)
Requires: pypi(azure_mgmt_security)
Requires: pypi(azure_mgmt_servicebus)
Requires: pypi(azure_mgmt_servicefabric)
Requires: pypi(azure_mgmt_signalr)
Requires: pypi(azure_mgmt_sql)
Requires: pypi(azure_mgmt_sqlvirtualmachine)
Requires: pypi(azure_mgmt_storage)
Requires: pypi(azure_mgmt_trafficmanager)
Requires: pypi(azure_mgmt_web)
Requires: pypi(azure_multiapi_storage)
Requires: pypi(azure_storage_blob)
Requires: pypi(colorama)
Requires: pypi(cryptography)
Requires: pypi(fabric)
Requires: pypi(javaproperties)
Requires: pypi(jsmin)
Requires: pypi(jsondiff)
Requires: pypi(knack)
Requires: pypi(mock)
Requires: pypi(paramiko)
Requires: pypi(pyopenssl)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(scp)
Requires: pypi(six)
Requires: pypi(sshtunnel)
Requires: pypi(urllib3)
Requires: pypi(vsts_cd_manager)
Requires: pypi(websocket_client)
Requires: pypi(xmltodict)

%description python3
python3 components for the azure-cli package.


%prep
%setup -q -n azure-cli-2.5.1
cd %{_builddir}/azure-cli-2.5.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588961254
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-cli
cp %{_builddir}/azure-cli-2.5.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/azure-cli/7d8a62cc5b0bc6fd21840d3804a5d62b9e6f1366
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/az.bat
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/az
/usr/bin/az.completion.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-cli/7d8a62cc5b0bc6fd21840d3804a5d62b9e6f1366

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
