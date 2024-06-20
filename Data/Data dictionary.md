## A tabela users (dados sobre usuários):
 
* user_id — identificador exclusivo do usuário  
* first_name — nome do usuário  
* last_name — sobrenome do usuário  
* age — idade do usuário (em anos)  
* reg_date — data da inscrição (dd, mm, aa)  
* churn_date — a data que o usuário parou de usar o serviço (se o valor estiver ausente, isso significa que o  plano estava em uso quando o banco de dados foi extraído)  
* city — cidade de residência do usuário  
* plan — nome do plano  

## A tabela calls (dados sobre as chamadas):
 
* id — identificador de chamada exclusivo
* call_date — data da chamada
* duration — duração da chamada (em minutos)
* user_id — identificador do usuário que faz a chamada

## A tabela messages (dados sobre mensagens de texto):
 
* id — identificador exclusivo da mensagem de texto
* message_date — data da mensagem de texto
* user_id — identificador do usuário que envia a mensagem de texto

## A tabela internet (dados sobre sessões web):
 
* id — identificador exclusivo da sessão
* mb_used — volume de dados gasto durante a sessão (em megabytes)
* session_date — data da sessão web
* user_id — identificador do usuário

## A tabela plans (dados sobre os planos):
 
* plan_name — nome do plano
* usd_monthly_fee — preço mensal em dólares americanos
* minutes_included — pacote mensal de minutos
* messages_included — pacote mensal de mensagens de texto
* mb_per_month_included — volume do pacote de dados (em megabytes)
* usd_per_minute — preço por minuto depois de exceder o limite do pacote (por exemplo, se o pacote inclui 100 minutos, o primeiro minuto excedente será cobrado)
* usd_per_message — preço por mensagem de texto depois de exceder o limite do pacote
* usd_per_gb — preço por gigabyte extra de dados após exceder o limite do pacote (1 GB = 1.024 megabytes)