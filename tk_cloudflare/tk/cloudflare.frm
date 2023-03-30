VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   8505
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   19125
   LinkTopic       =   "Form1"
   ScaleHeight     =   8505
   ScaleWidth      =   19125
   StartUpPosition =   3  'µ¡¤f¯Ê¬Ù
   Begin VB.Frame Frame5 
      Caption         =   "Frame5"
      Height          =   3255
      Left            =   12600
      TabIndex        =   4
      Top             =   5160
      Width           =   6375
      Begin VB.CommandButton add 
         Caption         =   "add"
         Height          =   375
         Left            =   3120
         TabIndex        =   10
         Top             =   240
         Width           =   1335
      End
      Begin VB.CommandButton search 
         Caption         =   "search"
         Height          =   375
         Left            =   1680
         TabIndex        =   9
         Top             =   240
         Width           =   1335
      End
      Begin VB.CommandButton getdomain 
         Caption         =   "getdomain"
         Height          =   375
         Left            =   240
         TabIndex        =   8
         Top             =   240
         Width           =   1335
      End
   End
   Begin VB.Frame Frame4 
      Caption         =   "Frame4"
      Height          =   3255
      Left            =   6480
      TabIndex        =   3
      Top             =   5160
      Width           =   5775
   End
   Begin VB.Frame Frame3 
      Caption         =   "Frame3"
      Height          =   4935
      Left            =   12600
      TabIndex        =   2
      Top             =   120
      Width           =   6375
      Begin VB.TextBox Text1 
         Height          =   4575
         Left            =   120
         TabIndex        =   7
         Text            =   "Text1"
         Top             =   240
         Width           =   6135
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "Frame2"
      Height          =   4935
      Left            =   6480
      TabIndex        =   1
      Top             =   120
      Width           =   5775
      Begin VB.Label Label1 
         Caption         =   "Label1"
         Height          =   4575
         Left            =   120
         TabIndex        =   6
         Top             =   240
         Width           =   5655
      End
   End
   Begin VB.Frame domainListFrame 
      Caption         =   "domainList"
      Height          =   8295
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   6015
      Begin VB.ListBox List1 
         Height          =   7980
         Left            =   120
         TabIndex        =   5
         Top             =   240
         Width           =   5775
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()

End Sub

Private Sub Text1_Change()

End Sub
