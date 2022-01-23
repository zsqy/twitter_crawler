import twint

c4 = twint.Config()
c4.Search = ['malaysia']
c4.Limit = '10000'
c4.Lang = 'en'
#c4.Since = '2022-01-01'
#c4.Until = '2022-01-22'
c4.Store_csv = True
c4.Output = "out"
twint.run.Search(c4)


#c8 = twint.Config()
#c8.Search = ['covid', 'kuala lumpur']
#c8.Limit = '10000000'
#c8.Lang = 'en'
##c8.Since = '2022-01-01'
##c8.Until = '2022-01-22'
#c8.Store_csv = True
#c8.Output = "out"
#twint.run.Search(c8)
