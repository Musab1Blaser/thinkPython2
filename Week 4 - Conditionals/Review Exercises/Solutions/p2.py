def will_my_report_be_checked():
    project_name = input()
    report_name = input()
    report_num = input()
    if project_name != "ThinkPython": #if project name is wrong then output No and stop execution
        print("No")
        return
    desired_report_name = "report"+report_num+".tex"
    if report_name != desired_report_name: #if report name is wrong then output No and stop execution
        print("No")
        return
    #if program reached till here then project name and report name must be correct
    print("Yes")

will_my_report_be_checked()