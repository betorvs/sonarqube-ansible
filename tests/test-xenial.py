import testinfra

def test_sonarqube_file(host):
    sonarqube = host.file("/opt/sonarqube-7.9.1/conf/sonar.properties")
    assert sonarqube.user == "sonarqube"
    assert sonarqube.group == "sonarqube"
    assert sonarqube.mode == 0o644


def test_openjdk_is_installed(host):
    openjdk = host.package("openjdk-8-jdk")
    assert openjdk.is_installed


def test_sonarqube_enabled(host):
    sonarqube = host.service("sonarqube")
    assert sonarqube.is_enabled