import flet as ft

def main(page: ft.Page):
    page.title = "Flet Basic Counter App" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    # 앱의 상태 (State) 초기화
    current_value = 0

    #이벤트 핸들러 함수 정의하기
    def update_counter(e):
        nonlocal current_value

        if e.control.data == "plus":
            current_value += 1
        elif e.control.data == "minus":
            current_value -= 1
        txt_number.value = str(current_value)
        page.update()
       

    

      # 1. 앱 제목을 위한 Text 컨트롤
    txt_title = ft.Text(
        value=page.title, 
        size=24, 
        weight=ft.FontWeight.W_600,
        color=ft.Colors.BLACK87
    )
    
    # 2. 카운트 값을 표시할 Text 컨트롤
    txt_number = ft.Text(
        value=str(current_value), # 초기값은 0
        size=40, 
        weight=ft.FontWeight.BOLD
    )

        # 감소 버튼 정의 
    minus_button = ft.IconButton(
        icon=ft.Icons.REMOVE,
        data="minus", # 이벤트 처리 시 버튼 식별용
        on_click=update_counter
    )
    # 증가 버튼 정의 
    plus_button = ft.IconButton(
        icon=ft.Icons.ADD,
        data="plus", # 이벤트 처리 시 버튼 식별용
        on_click=update_counter
    )


    # 3단계: 레이아웃 구성 및 페이지 추가
    # Row를 이용하여 버튼과 숫자를 배열
    counter_row = ft.Row(
        [
            minus_button,
            txt_number,
            plus_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    
    # Column을 사용하여 제목과 counter_row를 수직으로 배치
    main_column = ft.Column(
        [
            txt_title,      # 1. 제목 (맨 위)
            counter_row,    # 2. 카운터 (그 아래)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20 # 제목과 카운터 사이의 간격
    )

    # Column을 페이지에 추가
    page.add(main_column) 


ft.app(main, view=ft.AppView.WEB_BROWSER)
