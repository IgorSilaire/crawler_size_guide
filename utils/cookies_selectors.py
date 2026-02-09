# utils/cookies_selectors.py

ACCEPT_WORDS_FR = [
    "accepter",
    "j'accepte",
    "accepte",
    "tout accepter",
    "autoriser",
    "confirmer",
    "accord",
    "ok",
    "ok pour moi",
    "tous accepter"
]

COMMON_ACCEPT_SELECTORS = [
    # OneTrust
    "#onetrust-accept-btn-handler",
    "button#accept-recommended-btn-handler",
    ".onetrust-close-btn-handler",

    # Cookiebot
    "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
    "a#CybotCookiebotDialogBodyButtonAccept",

    # TrustArc
    "#truste-consent-button",
    ".truste-button1",

    # Generic patterns
    "button[id*='accept' i]",
    "button[class*='accept' i]",
    "button[class*='consent' i]"
]

IFRAME_ACCEPT_SELECTORS = [
    "button[title*='Accept' i]",
    "button:has-text('Accepter')",
    "button:has-text('Tout accepter')",
    "button:has-text('J\\'accepte')",
    "button[class*='accept' i]"
]
