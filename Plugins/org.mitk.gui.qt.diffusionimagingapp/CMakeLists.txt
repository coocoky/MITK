if(MITK_USE_QT_WEBENGINE)
  # The project name must correspond to the directory name of your plug-in
  # and must not contain periods.
  project(org_mitk_gui_qt_diffusionimagingapp)

  mitk_create_plugin(
    EXPORT_DIRECTIVE DIFFUSIONIMAGING_APP_EXPORT
    EXPORTED_INCLUDE_SUFFIXES src
    MODULE_DEPENDS MitkQtWidgets MitkSceneSerialization
    PACKAGE_DEPENDS Qt5|WebEngineWidgets
  )
endif()
