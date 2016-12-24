package com.playonlinux.javafx;


import com.phoenicis.library.LibraryConfiguration;
import com.playonlinux.apps.AppsConfiguration;
import com.playonlinux.configuration.PlayOnLinuxGlobalConfiguration;
import com.playonlinux.engines.EnginesConfiguration;
import com.playonlinux.javafx.controller.ControllerConfiguration;
import com.playonlinux.javafx.views.ViewsConfiguration;
import com.playonlinux.javafx.views.setupwindow.JavaFXSetupWindowUIConfiguration;
import com.playonlinux.scripts.ScriptsConfiguration;
import com.playonlinux.tools.ToolsConfiguration;
import com.playonlinux.win32.Win32Configuration;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

@Configuration
@Import({
        PlayOnLinuxGlobalConfiguration.class,
        ControllerConfiguration.class,
        ScriptsConfiguration.class,
        ViewsConfiguration.class,
        AppsConfiguration.class,
        EnginesConfiguration.class,
        LibraryConfiguration.class,
        JavaFXSetupWindowUIConfiguration.class,
        Win32Configuration.class,
        ToolsConfiguration.class
})
class AppConfiguration {


}
