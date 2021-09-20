## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yes i am
- yes i'm

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- no i am not
- no i'm not

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

<!-- user defined intents -->
## intent:make_appiontment
- [appointment](reservation)
- new [appointment](reservation)
- [make](option) [appointment](reservation)
- [place](option) [appointment](reservation)

- i want an [appointment](reservation)
- i want a new [appointment](reservation)
- i need an [appointment](reservation)
- i need a new [appointment](reservation)

- i want to [make](option) an [appointment](reservation)
- i want to [meet](option) a [doctor](service_person)
- i want to [make](option) an [appointment](reservation) to meet a [doctor](service_person)
- i need to [make](option) an [appointment](reservation)
- i need to [meet](option) a [doctor](service_person)
- i need to [place](option) an [appointment](reservation) to meet a [dr](service_person)
- i want to [place](option) an [appointment](reservation)
- i want to [place](option) an [appointment](reservation) to meet a [dr.](service_person)

## intent:change_appiontment
- [change](option) [appointment](reservation)
- [postpone](option) [appointment](reservation)

- i want to [change](option) [appointment](reservation)
- i need to [postpone](option) [appointment](reservation)
- i want to [change](option) [appointment](reservation)
- i need to [postpone](option) [appointment](reservation)

- i want to [postpone](option) my [appointment](reservation)
- i need to [postpone](option) my [appointment](reservation)

- i want to [postpone](option) my [appointment](reservation)
- i want to [change](option) my [appointment](reservation) [03/02](date)
- i need to [postpone](option) my [appointment](reservation)
- i need to [change](option) my [appointment](reservation) [04-13](date)
- i want to [postpone](option) my [appointment](reservation) with [4-1](date)
- i want to [change](option) my [appointment](reservation) on [2021-5-23](date)
- i need to [postpone](option) my [appointment](reservation) 
- i need to [change](option) my [appointment](reservation) on [2021/11/13](date)

## intent:delete_appointment
- [cancel](option) [appointment](reservation)
- [delete](option) [appointment](reservation)

- i want to [cancel](option) my [appointment](reservation)
- i need to [cancel](option) my [appointment](reservation)
- i want to [cancel](option) my [appointment](reservation) with [doctor](service_person) 
- i want to [cancel](option) my [appointment](reservation) with [dr.](service_person)
- i need to [cancel](option) my [appointment](reservation) with [doctor](service_person
- i need to [cancel](option) my [appointment](reservation) with [dr](service_person)

- i want to [cancel](option) my [appointment](reservation)
- i want to [cancel](option) my [appointment](reservation) on [date](date)
- i need to [cancel](option) my [appointment](reservation)
- i need to [cancel](option) my [appointment](reservation) on [date](date)
- i want to [cancel](option) my [appointment](reservation) with [doctor](service_person)
- i want to [cancel](option) my [appointment](reservation) on [date](date) with [dr.](service_person)
- i need to [cancel](option) my [appointment](reservation) with [doctor](service_person
- i need to [cancel](option) my [appointment](reservation) on [date](date) with [doctor](service_person)

- i want to [delete](option) my [appointment](reservation)
- i need to [delete](option) my [appointment](reservation)
- i want to [delete](option) my [appointment](reservation) with [dr](service_person)
- i want to [delete](option) my [appointment](reservation) with [doctor](service_person)

## intent:check_appointment
- show me my [appointment](reservation)
- show me my [appointment](reservation) on [2021/11/12](date)
- show me my [appointments](reservation) [today](relativedate)

- who wants to meet me [today](relativedate)
- who wants to meet me at [5.00](time) [tomorrow](relativedate)
- who is waiting to meet me on [tomorrow](relativedate)

- do i have [appointments](reservation) at [14.00](time)
- is there any [appoinment](reservation) on [2022-9-8](date)
- are there [appoinments](reservation) on [2022-9-8](date)

## intent:get_report
- i need my [report](deliverable)
- i need to get my [report](deliverable)
- send me my [report](deliverable)
- show me the [report](deliverable)
- issue my [report](deliverable)
- is my [report](deliverable) available?
- where is my [report](deliverable) ?
- i need all of my [patients](client_person) [reports](deliverable)
- i need [reports](deliverable) issued by me

- i want my [report](deliverable)
- i want to get my [report](deliverable)

## intent:inform_name
- [dr](service_person) [kamal](person_name)
- [dr.](service_person) [kamal](person_name)
- [dr](service_person) [saman](person_name)
- [dr.](service_person) [saman](person_name)
- [dr](service_person) [jayawardana](person_name)
- [dr.](service_person) [jayawardana](person_name)
- [dr](service_person) [dissaneyake](person_name)
- [dr.](service_person) [rathnasiri](person_name)

- [doctor](service_person) [susantha](person_name)
- [doctor](service_person) [jayanath](person_name)
- [doctor](service_person) [prasad](person_name)
- [doctor](service_person) [vimala](person_name)
- [doctor](service_person) [sanduni](person_name)
- [doctor](service_person) [vishaka](person_name)
- [doctor](service_person) [lochana](person_name)
- [doctor](service_person) [dilani](person_name)

- [kavindu](person_name)
- [dulaj](person_name)
- [rathnaweera](person_name)
- [rathnayeka](person_name)
- [adhikari](person_name)
- [samantha](person_name)
- [hansi](person_name)
- [suranga](person_name)
- [lakmal](person_name)
- [chamath](person_name)
- [lakshman](person_name)
- [supun](person_name)
- [sarath](person_name)
- [fernando](person_name)
- [kesara](person_name)
- [pasindu](person_name)
- [hiruni](person_name)

##  intent:inform_usertype
- [patient](client_person)
- [doctor](service_person)
- i am a [patient](client_person)
- i am a[doctor](service_person)
- im a [patient](client_person)
- im a [doctor](service_person)
- i'm a [patient](client_person)
- i'm a [doctor](service_person)

## intent:inform_date
- [2031-04-05](date)
- [7-05](date)
- [2041/04/05](date)
- [04/05](date)


## intent:inform_time
- [04:34](time)
- [15:30](time)
- [11:22](time)
- [19:50](time)

- [04.34](time)
- [15.30](time)
- [11.22](time)
- [19.50](time)

- [4.20](time)
- [5.00](time)
- [1.23](time)
- [9.05](time)

## intent:inform_relativetime
- [today](relativedate)
- [tomorrow](relativedate)
- [tomorrow](relativedate) at [5.00](time)
- [today](relativedate) [14.11](time)

- [today](relativedate)
- [tomorrow](relativedate)
- [tomorrow](relativedate) [after](refer_after) [5.00](time)
- [today](relativedate) [before](refer_before) [14.11](time)

- [after](refer_after) [5.00](time)
- [before](refer_before) [14.11](time)

- [after](refer_after) [2013-05-9](date)
- [before](refer_before) [2021/7/11](date)

## intent:inform_userhash
- [h5h3gkh2kl3g5256g5gk22lk6](userhash)
- [j25k6kk32oi9g9080r9egs09ggsd](userhash)
- [5kk345kk62kk62l62jjhj2](userhash)
- [45889gfg9834u987gdt83reg](userhash)
- [feoguow3thogotoirgw5f67](userhash)

## intent:inform_reporthash
- [report_h5h3gkh2kl3g5256g5gk22lk6](reporthash)
- [report_j25k6kk32oi9g9080r9egs09ggsd](reporthash)
- [report_5kk345kk62kk62l62jjhj2](reporthash)
- [report_45889gfg9834u987gdt83reg](reporthash)
- [report_feoguow3thogotoirgw5f67](reporthash)

## regex:userhash
- ([0-9]|[a-z]){20-30}

## regex:reporthash
- report_([0-9]|[a-z]){20-30}
## regex:date
- [0-9]{4}-((0[0-9]|[0-9])|1[0-2])-[0-2][0-9]|[3][0-1]
- ((0[0-9]|[0-9])|1[0-2])-([0-2][0-9]|[3][0-1])
- [0-9]{4}/((0[0-9]|[0-9])|1[0-2])/[0-2][0-9]|[3][0-1]
- ((0[0-9]|[0-9])|1[0-2])/([0-2][0-9]|[3][0-1])

## regex:time
- ((0[0-9]|[0-9])|1[0-9]|2[0-3]):[0-5][0-9]
- ((0[0-9]|[0-9])|1[0-9]|2[0-3]).[0-5][0-9]

