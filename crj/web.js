  
  var obj = {
  'left_ail':0.2,
  'right_ail':-0.15,
  'left_elev':1.0,
  'right_elev':1.0,
  'rudder':0.0,
  'leftflap':0,
  'rightflap':0,
  'ailtrim':-2.0,
  'stabtrim':3,
  'ruddertrim':4
  };

  function init()
  {
	document.myform.url.value = "ws://localhost:8000/";
	document.myform.inputtext.value = JSON.stringify(obj);
	document.myform.disconnectButton.disabled = true;
  }

  function doConnect()
  {
    websocket = new WebSocket(document.myform.url.value);
    websocket.onopen = function(evt) { onOpen(evt) };
    websocket.onclose = function(evt) { onClose(evt) };
    websocket.onmessage = function(evt) { onMessage(evt) };
    websocket.onerror = function(evt) { onError(evt) };
  }

  function onOpen(evt)
  {
    writeToScreen("connected\n");
	document.myform.connectButton.disabled = true;
	document.myform.disconnectButton.disabled = false;
  }

  function onClose(evt)
  {
    writeToScreen("disconnected\n");
	document.myform.connectButton.disabled = false;
	document.myform.disconnectButton.disabled = true;
  }

  function onMessage(evt)
  {
    //writeToScreen("response: " + evt.data + '\n');
    obj = JSON.parse(evt.data);

    //writeToScreen("left elevator: " + obj.left_elev);
    //writeToScreen("right elevator: " + obj.right_elev);
    //writeToScreen("left aileron: " + obj.left_ail);
    //writeToScreen("right aileron: " + obj.right_ail);

    setflappos(obj.leftflap,obj.rightflap);

    setelevpos(obj.left_elev,obj.right_elev);

    setailpos(obj.left_ail,obj.right_ail);

    setrudderpos(obj.rudder);

    setstabtrim(obj.stabtrim);
    setrolltrim(obj.ailtrim);
    setruddertrim(obj.ruddertrim);
    setspoilersAll(obj.spoilersAll);
    

  }

  function onError(evt)
  {
    writeToScreen('error: ' + evt.data + '\n');

	websocket.close();

	document.myform.connectButton.disabled = false;
	document.myform.disconnectButton.disabled = true;

  }

  function doSend(message)
  {
   message='fc';
    writeToScreen("sent: " + message + '\n'); 
    websocket.send(message);
  }


  function writeToScreen(message)
  {
    message = message + '\n';
    document.myform.outputtext.value += message
	document.myform.outputtext.scrollTop = document.myform.outputtext.scrollHeight;

  }

  window.addEventListener("load", init, false);


   function sendText() {
		doSend( document.myform.inputtext.value );
   }

  function clearText() {
		document.myform.outputtext.value = "";
   }

   function doDisconnect() {
		websocket.close();
   }