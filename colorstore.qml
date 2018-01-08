import QtQuick 2.1
import QtQuick.Controls 1.4
import Qt.labs.settings 1.0

ApplicationWindow {
    id: window
    x:10
    y:10

    width: 500
    height: 600
    flags: Qt.Window | Qt.WindowTitleHint | Qt.WindowStaysOnTopHint
            | Qt.WindowCloseButtonHint
        modality: Qt.NonModal
    menuBar: MenuBar {
        Menu {
            title: qsTr('File')
            MenuItem {
                text: qsTr('&Test')
                onTriggered: console.log('test')
            }
            MenuItem {
                text: qsTr('&Exit')
                onTriggered: Qt.quit();
            }
        }
    }

    Button {
            id:btn1
            text: "full fullscreen"
            anchors.left: parent
            onClicked: showFullScreen()
        }
    Button {
            id:btn2
            text: "minimize screen"
            anchors.left: btn1.right
            onClicked: showMinimized()
        }
    Image {
        source: "./fish.png"
        id: draggable
        //color: "blue"
        width: 50
        height: 50
        x:Math.round(Math.random()*500)
        y:Math.round(Math.random()*500)
        //radius: 10

        onXChanged: {
            if (mouseArea.drag.active) {
                console.log("x=" + x);
                console.log(Math.round(Math.random()*100))}
        }
        onYChanged: {
            if (mouseArea.drag.active) {
              console.log("y=" + y)
            }
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            drag {
                target: draggable
                axis: Drag.XandYAxis
            }
        }
    }
}
