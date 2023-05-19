<a href="https://github.com/thenaim/ionic-whatsapp-clone">
  <p align="center">
    <img src="https://i.imgur.com/QcWvgs6.png">
  </p>
</a>

<h2 align="center">
  Introducing a open source WhatsApp app clone.
</h2>
<p align="center">
  Providing you with the components, templates, native components, ngrx, i18n, localStorage, themes, auth pages and much more  needed to build a mobile application on ionic framework.
</p>

# Getting started

```bash
git clone https://github.com/thenaim/ionic-whatsapp-clone myApp
cd myApp
npm i

# Build, before adding any native platforms 
ionic build

# Add ios
npx cap add ios

# Add Android
npx cap add android

# Browser (native not support)
ionic serve
```

# Run Capacitor or see [docs](https://ionicframework.com/docs/cli/commands/capacitor-run)
```bash
# Open Android
npx cap open android

# Open iOS
npx cap open ios
```

### iOS Setup

Download and install [Xcode](https://developer.apple.com/xcode/).

Then make sure the command-line tools are selected for use:

```bash
xcode-select --install
```

And you need to install some utilities:

```bash
npm install -g ios-sim
npm install -g ios-deploy
```

# Android Setup

Download and install:

- [JDK8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
- [Gradle](https://gradle.org/install/)
- [Android Studio](https://developer.android.com/studio/)

Then install Android SDK on Android Studio and configure the [environment variables](https://developer.android.com/studio/command-line/variables) (`ANDROID_SDK_ROOT`).

## Supporting platforms

In pursuit of [adaptive styling](https://ionicframework.com/docs/core-concepts/fundamentals#adaptive-styling), Ionic fully supports and is well tested on the mobile platforms listed below:

| Platform | Version |
| - | - |
| **Android** | 5.0+ |
| **iOS** | 11.0+ |

See [Ionic Docs](https://ionicframework.com/docs/reference/browser-support) for more information.

## WhatsApp UI Screens Sketch

Figma: [WhatsApp UI](https://www.figma.com/community/file/874576344344319149)

Creator: [Pixsellz](https://pixsellz.io/)

## Contributors

Want to start contributing to open source with ionic? Leave your mark and join the growing team of contributors!

Get started by checking out list of open [issues](https://github.com/thenaim/ionic-whatsapp-clone/issues) and reading [Contributor Guide](https://github.com/thenaim/ionic-whatsapp-clone/blob/master/CONTRIBUTING.md)

## License

License MIT (see the [LICENSE](https://github.com/thenaim/ionic-whatsapp-clone/blob/master/LICENSE) file for the full text)
