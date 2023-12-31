from seedsigner.controller import Controller

# l10n
import gettext
i18n = gettext.translation("seedsigner", './seedsigner/locales', fallback=True, languages=['ko','en'])
i18n.install()


# Get the one and only Controller instance and start our main loop
Controller.get_instance().start()
