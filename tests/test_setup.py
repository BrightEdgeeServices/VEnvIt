import pytest


@pytest.mark.setup
class TestSetupVenVitApp:
    def test_venvit_app_defaults(self):
        """VenVitApp should default both versions to None."""
        from venvit.setup import VenVitApp

        app = VenVitApp()

        assert app.curr_ver is None
        assert app.latest_ver is None

    def test_venvit_app_with_values(self):
        """VenVitApp should store provided version values."""
        from venvit.setup import VenVitApp

        app = VenVitApp(curr_ver="1.0.0", latest_ver="2.0.0")

        assert app.curr_ver == "1.0.0"
        assert app.latest_ver == "2.0.0"
