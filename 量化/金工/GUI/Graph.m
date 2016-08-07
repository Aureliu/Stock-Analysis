function varargout = Graph(varargin)
% GRAPH MATLAB code for Graph.fig
%      GRAPH, by itself, creates a new GRAPH or raises the existing
%      singleton*.
%
%      H = GRAPH returns the handle to a new GRAPH or the handle to
%      the existing singleton*.
%
%      GRAPH('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GRAPH.M with the given input arguments.
%
%      GRAPH('Property','Value',...) creates a new GRAPH or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Graph_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Graph_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Graph

% Last Modified by GUIDE v2.5 07-Apr-2016 15:38:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Graph_OpeningFcn, ...
                   'gui_OutputFcn',  @Graph_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Graph is made visible.
function Graph_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Graph (see VARARGIN)
 set(handles.uipanel1,'parent',handles.figure1,'Position',get(handles.uipanel2,'Position'));
% set(handles.uipanel2,'parent',gcf);
% set(handles.uipanel3,'parent',gcf);
 set(handles.uipanel2,'Parent',gcf);
set(handles.uipanel3,'Parent',handles.figure1,'Position',get(handles.uipanel2,'Position'));
set(handles.uipanel4,'Parent',handles.figure1,'Position',get(handles.uipanel2,'Position'));
set(handles.uipanel1,'Visible','off');
set(handles.uipanel2,'Visible','off');
set(handles.uipanel3,'Visible','off');
set(handles.pushbutton1,'Visible','off');
set(handles.pushbutton3,'Visible','off');
set(handles.pushbutton7,'Visible','off');
set(handles.pushbutton8,'Visible','off');
set(handles.pushbutton9,'Visible','off');
set(handles.pushbutton10,'Visible','off');
set(handles.pushbutton11,'Visible','on');
set(handles.pushbutton12,'Visible','on');
set(handles.radiobutton1,'Visible','on');
set(handles.edit1,'Visible','on');
set(handles.edit2,'Visible','on');
set(handles.text2,'Visible','on');
set(handles.text3,'Visible','on');
set(handles.pushbutton13,'Visible','on');
set(handles.uipanel4,'Visible','on');

% Choose default command line output for Graph
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Graph wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Graph_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.uipanel1,'Visible','off');
set(handles.uipanel2,'Visible','off');
set(handles.uipanel3,'Visible','off');
set(handles.pushbutton1,'Visible','off');
set(handles.pushbutton3,'Visible','off');
set(handles.pushbutton7,'Visible','off');
set(handles.pushbutton8,'Visible','off');
set(handles.pushbutton9,'Visible','off');
set(handles.pushbutton10,'Visible','off');
set(handles.pushbutton11,'Visible','on');
set(handles.pushbutton12,'Visible','on');
set(handles.radiobutton1,'Visible','on');
set(handles.edit1,'Visible','on');
set(handles.edit2,'Visible','on');
set(handles.text2,'Visible','on');
set(handles.text3,'Visible','on');
set(handles.pushbutton13,'Visible','on');
set(handles.uipanel4,'Visible','on');


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton8.
function pushbutton8_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.uipanel1,'Visible','on');
set(handles.uipanel2,'Visible','off');
set(handles.uipanel3,'Visible','off');

% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.uipanel1,'Visible','off');
set(handles.uipanel2,'Visible','on');
set(handles.uipanel3,'Visible','off');


% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.uipanel1,'Visible','off');
set(handles.uipanel2,'Visible','off');
set(handles.uipanel3,'Visible','on');


% --- Executes on button press in pushbutton11.
function pushbutton11_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton12.
function pushbutton12_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton13.
function pushbutton13_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.uipanel1,'Visible','on');
set(handles.uipanel2,'Visible','on');
set(handles.uipanel3,'Visible','on');
set(handles.pushbutton1,'Visible','on');
set(handles.pushbutton3,'Visible','on');
set(handles.pushbutton7,'Visible','on');
set(handles.pushbutton8,'Visible','on');
set(handles.pushbutton9,'Visible','on');
set(handles.pushbutton10,'Visible','on');
set(handles.pushbutton11,'Visible','off');
set(handles.pushbutton12,'Visible','off');
set(handles.radiobutton1,'Visible','off');
set(handles.edit1,'Visible','off');
set(handles.edit2,'Visible','off');
set(handles.text2,'Visible','off');
set(handles.text3,'Visible','off');
set(handles.pushbutton13,'Visible','off');
set(handles.uipanel4,'Visible','off');
