import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtLocation 5.9
import QtPositioning 5.8
import QtQuick.Layouts 1.3

Window{
id: mainWindow
width: 512
height: 512
visible: true

ListModel{
    id:dummyModel
    ListElement {
        Latitude: 47.212047
        Longitude: -1.551647
        Label: "something"
        Orientation: 0
        Color:"transparent"
    }
}

Plugin {
    id: googleMaps
    name: "esri" // "mapboxgl", "esri", ...
    // specify plugin parameters if necessary
     //PluginParameter {
         //name:"mapboxgl"
         //name:"googlemaps.maps.apikey"
         //value:"AIzaSyDosXFZr-0v1hwxq_b60QWHqeegDxIDasM"
     //}

}

Map {
    id: myMap
    anchors.fill: parent
    plugin: googleMaps
    activeMapType: supportedMapTypes[1]

    center: QtPositioning.coordinate(59.92, 10.77) // Oslo
    zoomLevel: 14

    MapItemView{
        id:dynamicMapObject
        model: dummyModel
        delegate: MapQuickItem {
            coordinate: QtPositioning.coordinate(Latitude,Longitude)
            /*sourceItem:  Text{
                width: 100
                height: 50
                text: model.Label
                rotation: model.Orientation
                opacity: 0.6
                color: model.Color
            }*/
            sourceItem: Image {
                id: imageMap
                source: "pinForMap.png"
            }
        }
    }

    MapPolyline {
            id:myPolyLine
            line.width: 3
            line.color: 'green'
            path: [
                { latitude: 59.92, longitude: 10.77 },
                { latitude: 59.96, longitude: 10.78 },
                { latitude: 59.99, longitude: 10.76 },
                { latitude: 59.95, longitude: 10.74 }
            ]
    }

    MapCircle {
      id:prova
      center: myMap.center.atDistanceAndAzimuth(100,90)
      opacity:0.8
      border.color:"green"
      border.width: 4
      radius:300

    }
}

MouseArea {
       anchors.fill: parent
       acceptedButtons:  Qt.RightButton

       onClicked: {
            if (mouse.button === Qt.RightButton)
            {
                lbl1.text="Latitude:"+myMap.toCoordinate(Qt.point(mouseX,mouseY)).latitude
                lbl2.text="Longitude:"+myMap.toCoordinate(Qt.point(mouseX,mouseY)).longitude
                dummyModel.append({
                    "Latitude": myMap.toCoordinate(Qt.point(mouseX,mouseY)).latitude ,"Longitude": myMap.toCoordinate(Qt.point(mouseX,mouseY)).longitude ,
                                      Image: {source: "file://pinForMap.png"} , "Color": "red",
                    "Orientation":Number(3), }) //"Label": "abc" , "Color": "red",
            }
       }
}

Rectangle{
    anchors.right: parent.right
    color: "lightgray"
    width: 180;height: 40
    ColumnLayout{
        Label{
            id:lbl1
            anchors.horizontalCenter: parent.horizontalCenter
            color: "green"
            text: "Deneme"
        }
        Label{
            id:lbl2
            anchors.horizontalCenter: parent.horizontalCenter
            color: "green"
            text: "Deneme"
        }
    }
}
Button{
    id:buttonMap
    text:"Click to add name"
    onClicked: {
        if(buttonMap.text == "Click to add name")
        {
            buttonMap.text = "Click to cancel name"
            myMap.activeMapType = myMap.supportedMapTypes[3]
        }
        else
        {
            buttonMap.text = "Click to add name"
            myMap.activeMapType = myMap.supportedMapTypes[1]
        }
    }
}

GroupBox{
       title:"map types"
       ComboBox{
           model:myMap.supportedMapTypes
           textRole:"description"
           onCurrentIndexChanged: myMap.activeMapType = myMap.supportedMapTypes[currentIndex]
       }
 }
}
