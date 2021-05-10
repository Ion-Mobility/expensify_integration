[<#lt>
<#list reports as report>
    {<#lt>
        "title":"${report.reportName}",<#lt>
        "employee_name":"${report.submitter.fullName}",<#lt>
        "expense_approver":"${report.managerEmail}",<#lt>
        "posting_date":"${report.submitted}",<#lt>
        "expenses":[<#lt>
        <#list report.transactionList as expense>
            {<#lt>
                "amount":"${expense.amount}",<#lt>
                "expense_type":"${expense.category}",<#lt>
                "description":"${expense.comment}",<#lt>
                "expense_date":"${expense.created}",<#lt>
            }<#sep>,</#sep><#lt>
        </#list>]<>
    }<#sep>,</#sep><#lt>
</#list>]