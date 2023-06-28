# Suponha que o preço de capa de um livro seja R$ 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.

book_price = 24.20
bookstore_price = 24.20 - 24.20 * 0.4 
transport_price = 0.75 * 59 + 3
amount_book_price = bookstore_price * 60

total_cost = amount_book_price + transport_price 
print(total_cost)
