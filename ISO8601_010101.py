T = int(input())
date = []
for i in range(0,T):
    date.append(input())

for i in range(0,T):
    start_year = 1
    start_mon = 1
    start_day = 1
    start_date = 1 #MON
    passed_day = 0
    target_year = int(date[i][:4])
    target_mon = int(date[i][4:6])
    target_day = int(date[i][6:])
    cnt_print = 0
    print('{}년 {}월 {}일은'.format(target_year, target_mon, target_day, end=' '))
    while start_year < target_year:
        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
            passed_day+=366
            start_year+=1
        else:
            passed_day+=365
            start_year+=1
    
    if target_mon == 1:
        passed_day+=0
    elif target_mon == 2: 
        passed_day+=31
    elif target_mon == 3:
        passed_day+=59
    elif target_mon == 4:
        passed_day+=90
    elif target_mon == 5:
        passed_day+=120
    elif target_mon == 6:
        passed_day+=151
    elif target_mon == 7:
        passed_day+=181
    elif target_mon == 8:
        passed_day+=212
    elif target_mon == 9:
        passed_day+=243
    elif target_mon == 10:
        passed_day+=273
    elif target_mon == 11:
        passed_day+=304
    elif target_mon == 12:
        passed_day+=334
    
    if (target_year % 4 == 0 and target_year % 100 != 0) or (target_year % 400 == 0):
        if target_mon > 2:
            passed_day+=1
    date_idx = passed_day % 7

    #해당일이 마지막 주이면서 다음달의 첫주인 경우 먼저 예외 처리
    if ((target_mon == 1 or target_mon == 3 or target_mon == 5 or target_mon == 7 or target_mon == 8 or target_mon == 10 or target_mon == 12) and target_day>=29):
        if (target_day == 29 and date_idx == 0) or (target_day == 30 and (date_idx == 0 or date_idx == 1)) or (target_day == 31 and (date_idx == 0 or date_idx == 1 or date_idx == 2)):
            if target_mon == 12:
                print('{}년 1월 1째주 입니다.'.format(target_year+1))
                cnt_print = 1
            else:
                print('{}월 1째주 입니다.'.format(target_mon+1))
                cnt_print = 1
    elif ((target_mon == 4 or target_mon == 6 or target_mon == 9 or target_mon == 11) and target_day>=28): #4,6,9,11월 이면
        if (target_day == 28 and date_idx == 0) or (target_day == 29 and  (date_idx == 0 or date_idx == 1)) or (target_day == 30 and (date_idx == 0 or date_idx == 1 or date_idx == 2)):
            print('{}월 1째주 입니다.'.format(target_mon+1))
            cnt_print = 1
    elif target_mon == 2 and target_day>=26:
        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
            if (target_day == 27 and date_idx == 0) or (target_day == 28 and  (date_idx == 0 or date_idx == 1)) or (target_day == 29 and (date_idx == 0 or date_idx == 1 or date_idx == 2)):
                print('{}월 1째주 입니다.'.format(target_mon+1))
                cnt_print = 1
        else:
            if (target_day == 26 and date_idx == 0) or (target_day == 27 and  (date_idx == 0 or date_idx == 1)) or (target_day == 28 and (date_idx == 0 or date_idx == 1 or date_idx == 2)):
                print('{}월 1째주 입니다.'.format(target_mon+1))
                cnt_print = 1
    #
    if cnt_print == 0:
        if date_idx < 4: #그 달 1일이 첫주차인경우
            if date_idx == 0: #1일이 월요일인 경우
                print('{}월 {}째주 입니다.'.format(target_mon, ((target_day-1)//7)+1))
            elif date_idx == 1: #1일이 화요일인 경우
                print('{}월 {}째주 입니다.'.format(target_mon, (target_day//7)+1))
            elif date_idx == 2: #1일이 수요일인 경우
                print('{}월 {}째주 입니다.'.format(target_mon, ((target_day+1)//7)+1))
            elif date_idx == 3: #1일이 목요일인 경우
                print('{}월 {}째주 입니다.'.format(target_mon, ((target_day+2)//7)+1))
                
        else: #그 달 1일이 금,토,일 중일 경우
            b_mon = target_mon-1
            if date_idx == 5: #1일이 토요일인 경우
                if target_day < 3:
                    if b_mon == 1 or b_mon == 3 or b_mon == 5 or b_mon == 7 or b_mon == 8 or b_mon == 10:
                        #전달의 31일이 금요일
                        #전달의 1일은 수요일
                        #1수목금토5일 6월 13월 20월 27월
                        print('{}월 5째주 입니다.'.format(target_mon-1))
                    elif b_mon == 0:
                        #작년 12월의 31일이 금요일
                        #작년 12월의 1일은 수요일
                        #1수목금토5일 6월 13월 20월 27월
                        print('{}년 12월 5째주 입니다.'.format(target_year-1))
                    elif b_mon == 4 or b_mon == 6 or b_mon == 9 or b_mon == 11:
                        #전달의 30일이 금요일
                        #전달의 1일은 목요일
                        #1목2금3토4일 5월 12월 19월 26월
                        print('{}월 4째주 입니다.'.format(target_mon-1))
                    elif b_mon == 2:
                        #전달의 28이나 29가 금요일
                        #-----------------------
                        #28기준 1일은 토요일
                        #1토일 3월 10월 17월 24월
                        #-----------------------
                        #29기준 1일은 금요일 
                        #4월 11월 18월 25월
                        #즉 윤년에 관계없이 4주차
                        print('{}월 4째주 입니다.'.format(target_mon-1))
                else:  #3,10... 월요일이므로 -3
                    print('{}월 {}째주 입니다.'.format(target_mon, (target_day-3)//7+1))
                    
            elif date_idx == 6: #1일이 일요일인 경우
                if target_day == 1: #타겟이 1일(일요일) 이면
                    if b_mon == 1 or b_mon == 3 or b_mon == 5 or b_mon == 7 or b_mon == 8 or b_mon == 10:
                        #전달의 31일이 토요일
                        #전달의 1일은 목요일
                        #1목금토일 5월 12월 19월 26월 
                        print('{}월 5째주 입니다.'.format(target_mon-1))
                    elif b_mon == 0:
                        #작년 12월의 31일이 토요일
                        #작년 12월의 1일은 목요일
                        #1목금토일 5월 12월 19월 26월
                        print('{}년 12월 5째주 입니다.'.format(target_year-1))
                    elif b_mon == 4 or b_mon == 6 or b_mon == 9 or b_mon == 11:
                        #전달의 30일이 토요일
                        #전달의 1일은 금요일
                        #4월 11월 18월 25월
                        print('{}월 4째주 입니다.'.format(target_mon-1))
                    elif b_mon == 2:
                        #전달의 28이나 29가 토요일
                        #28기준 1일은 일요일
                        #2월 9월 16월 23월
                        #-----------------------
                        #29기준 1일은 토요일 
                        #3월 10월 17월 24월
                        #즉 윤년에 관계없이 4주차
                        print('{}월 4째주 입니다.'.format(target_mon-1))
                else: #2,9... 월요일이므로 -2
                    print('{}월 {}째주 입니다.'.format(target_mon, (target_day-2)//7+1))
                    
            elif date_idx == 4: #1일이 금요일인 경우
                if target_day < 4:
                    if b_mon == 1 or b_mon == 3 or b_mon == 5 or b_mon == 7 or b_mon == 8 or b_mon == 10:
                            #전달의 31일이 목요일
                            #전달의 1일은 화요일
                            #1화수목금토6일 7월 14월 21월 28월
                        print('{}월 5째주 입니다.'.format(target_mon-1))
                    elif b_mon == 0:
                            #작년 12월의 31일이 목요일
                            #작년 12월의 1일은 화요일
                            #1화수목금토6일 7월 14월 21월 28월
                        print('{}년 12월 5째주 입니다.'.format(target_year-1))
                    elif b_mon == 4 or b_mon == 6 or b_mon == 9 or b_mon == 11:
                            #전달의 30일이 목요일
                            #전달의 1일은 수요일
                            #1수목금토5일 6월 13월 20월 27월
                        print('{}월 5째주 입니다.'.format(target_mon-1))
                    elif b_mon == 2:
                            #전달의 28이나 29가 목요일
                            #28기준 1일은 금요일
                            #4월 11월 18월 25월
                            #-----------------------
                            #29기준 1일은 목요일 
                            #1목금토4일 5월 12월 19월 26월
                            #즉 윤년이 아니면 4주차
                            #윤년이면 5주차
                        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
                            print('{}월 5째주 입니다.'.format(target_mon-1))
                        else:
                            print('{}월 4째주 입니다.'.format(target_mon-1))
                            
                                           

                else: #4, 10... 월요일이므로 -4
                    print('{}월 {}째주 입니다.'.format(target_mon, (target_day-4)//7+1))

    
#기준일 하나를 잡고
#몇일 뒤인지 계산하여 해당 월의 1일 계산
#1583년 1월 1일은 토요일
#15830101 SAT
#20021228 ?
#1583+1584+ ... + 2000 + 2001 + 2002.01 + 2002.02 + ... + 2002.11
    
