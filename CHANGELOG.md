# Change Log

## [v0.7.4.2](https://github.com/Yelp/Tron/tree/v0.7.4.2) (2018-02-27)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.4.1...v0.7.4.2)

**Merged pull requests:**

- Fix tronview bug and include six in install\_requires [\#366](https://github.com/Yelp/Tron/pull/366) ([qui](https://github.com/qui))

## [v0.7.4.1](https://github.com/Yelp/Tron/tree/v0.7.4.1) (2018-02-23)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.4.0...v0.7.4.1)

**Closed issues:**

- Spanish translation [\#361](https://github.com/Yelp/Tron/issues/361)

**Merged pull requests:**

- Failure improvements [\#364](https://github.com/Yelp/Tron/pull/364) ([qui](https://github.com/qui))
- store the actionrun id in the status output by action\_runner [\#363](https://github.com/Yelp/Tron/pull/363) ([Rob-Johnson](https://github.com/Rob-Johnson))
- Ignore unknown ActionRuns [\#359](https://github.com/Yelp/Tron/pull/359) ([qui](https://github.com/qui))
- Upload to pypi on tags [\#357](https://github.com/Yelp/Tron/pull/357) ([solarkennedy](https://github.com/solarkennedy))
- Remove vagrant stuff [\#356](https://github.com/Yelp/Tron/pull/356) ([solarkennedy](https://github.com/solarkennedy))
- add stuck status for jobs [\#355](https://github.com/Yelp/Tron/pull/355) ([chlgit](https://github.com/chlgit))
- reconfigure jobs if monitoring setting has been updated [\#354](https://github.com/Yelp/Tron/pull/354) ([chlgit](https://github.com/chlgit))
- Python3 port 1/NaN [\#353](https://github.com/Yelp/Tron/pull/353) ([keymone](https://github.com/keymone))

## [v0.7.4.0](https://github.com/Yelp/Tron/tree/v0.7.4.0) (2018-02-13)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.3.2...v0.7.4.0)

**Closed issues:**

- Job Notifications [\#303](https://github.com/Yelp/Tron/issues/303)
- smtp with tls [\#257](https://github.com/Yelp/Tron/issues/257)
- nodes list [\#245](https://github.com/Yelp/Tron/issues/245)
- tronweb service view dashboard [\#243](https://github.com/Yelp/Tron/issues/243)
- support ec2 tag names for node\_pool [\#233](https://github.com/Yelp/Tron/issues/233)
- Consolidate documentation [\#135](https://github.com/Yelp/Tron/issues/135)
- Add 'owner' field to jobs [\#99](https://github.com/Yelp/Tron/issues/99)
- Tron daemon to run on slaves as an alternative to persistent SSH connections [\#81](https://github.com/Yelp/Tron/issues/81)
- Monitoring Framework [\#25](https://github.com/Yelp/Tron/issues/25)

**Merged pull requests:**

- \[wip\] Port to Python3 [\#352](https://github.com/Yelp/Tron/pull/352) ([keymone](https://github.com/keymone))
- Removed deprecated restart\_interval option [\#351](https://github.com/Yelp/Tron/pull/351) ([solarkennedy](https://github.com/solarkennedy))
- Removed mongodb support [\#350](https://github.com/Yelp/Tron/pull/350) ([solarkennedy](https://github.com/solarkennedy))
- Update readme to set expectations about tron development [\#349](https://github.com/Yelp/Tron/pull/349) ([solarkennedy](https://github.com/solarkennedy))
- Improve example cluster startup, and fix one remaining unicode error [\#348](https://github.com/Yelp/Tron/pull/348) ([qui](https://github.com/qui))

## [v0.7.3.2](https://github.com/Yelp/Tron/tree/v0.7.3.2) (2018-02-09)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.3.1...v0.7.3.2)

**Merged pull requests:**

- Twisted fix, example cluster and itest improvements [\#347](https://github.com/Yelp/Tron/pull/347) ([keymone](https://github.com/keymone))

## [v0.7.3.1](https://github.com/Yelp/Tron/tree/v0.7.3.1) (2018-02-09)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.3.0...v0.7.3.1)

## [v0.7.3.0](https://github.com/Yelp/Tron/tree/v0.7.3.0) (2018-02-08)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.2.0...v0.7.3.0)

**Merged pull requests:**

- Don't start tron on boot [\#345](https://github.com/Yelp/Tron/pull/345) ([keymone](https://github.com/keymone))
- Added dry-run and filtering on check\_tron\_jobs [\#344](https://github.com/Yelp/Tron/pull/344) ([solarkennedy](https://github.com/solarkennedy))
- Example cluster improvements [\#343](https://github.com/Yelp/Tron/pull/343) ([keymone](https://github.com/keymone))
- Make check\_tron\_jobs actually send alerts with lots of context [\#342](https://github.com/Yelp/Tron/pull/342) ([solarkennedy](https://github.com/solarkennedy))
- Local validation options, cleanup of unused functionality [\#340](https://github.com/Yelp/Tron/pull/340) ([keymone](https://github.com/keymone))
- first pass at adding pre-commit [\#321](https://github.com/Yelp/Tron/pull/321) ([Rob-Johnson](https://github.com/Rob-Johnson))

## [v0.7.2.0](https://github.com/Yelp/Tron/tree/v0.7.2.0) (2018-02-01)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.1.0...v0.7.2.0)

**Closed issues:**

- tron on OS X without Poll Reactor [\#305](https://github.com/Yelp/Tron/issues/305)
- allow viewing by host in tronview [\#138](https://github.com/Yelp/Tron/issues/138)

**Merged pull requests:**

- add coffeescript dependency to packaging image [\#341](https://github.com/Yelp/Tron/pull/341) ([Rob-Johnson](https://github.com/Rob-Johnson))
- run coffeescript compliation inside docker container; remove some unu… [\#339](https://github.com/Yelp/Tron/pull/339) ([Rob-Johnson](https://github.com/Rob-Johnson))
- Add option to delete namespaces in tronfig [\#338](https://github.com/Yelp/Tron/pull/338) ([qui](https://github.com/qui))
- Added monitoring dictionary for job configs [\#337](https://github.com/Yelp/Tron/pull/337) ([solarkennedy](https://github.com/solarkennedy))
- Added rerun for re-running jobs instead of restart [\#336](https://github.com/Yelp/Tron/pull/336) ([solarkennedy](https://github.com/solarkennedy))
- Added prototype check\_tron\_jobs command [\#335](https://github.com/Yelp/Tron/pull/335) ([solarkennedy](https://github.com/solarkennedy))
- add a json schema for describing tronfig [\#334](https://github.com/Yelp/Tron/pull/334) ([Rob-Johnson](https://github.com/Rob-Johnson))
- Handle configuration check requests [\#333](https://github.com/Yelp/Tron/pull/333) ([keymone](https://github.com/keymone))
- Bring back coffee [\#332](https://github.com/Yelp/Tron/pull/332) ([Rob-Johnson](https://github.com/Rob-Johnson))
- move from sysv-init to upstart [\#331](https://github.com/Yelp/Tron/pull/331) ([Rob-Johnson](https://github.com/Rob-Johnson))
- multi platform reactor; fix tests [\#330](https://github.com/Yelp/Tron/pull/330) ([Rob-Johnson](https://github.com/Rob-Johnson))
- encode command as utf-8 [\#329](https://github.com/Yelp/Tron/pull/329) ([Rob-Johnson](https://github.com/Rob-Johnson))

## [v0.7.1.0](https://github.com/Yelp/Tron/tree/v0.7.1.0) (2017-10-10)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.7.0.0...v0.7.1.0)

**Closed issues:**

- Unsafe use of `global`  in tron/serialize/runstate/yamlstore.py [\#326](https://github.com/Yelp/Tron/issues/326)
- Tron assumes USER environment variable is always available, and it isn't. [\#315](https://github.com/Yelp/Tron/issues/315)
- Use the yaml c-loader for moar speed \(when available\) [\#306](https://github.com/Yelp/Tron/issues/306)

**Merged pull requests:**

- dont assume the USER env var [\#328](https://github.com/Yelp/Tron/pull/328) ([Rob-Johnson](https://github.com/Rob-Johnson))
- Issues 306 & 326  [\#327](https://github.com/Yelp/Tron/pull/327) ([Rob-Johnson](https://github.com/Rob-Johnson))

## [v0.7.0.0](https://github.com/Yelp/Tron/tree/v0.7.0.0) (2017-08-25)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.2.0...v0.7.0.0)

**Merged pull requests:**

- create a make target for releasing [\#325](https://github.com/Yelp/Tron/pull/325) ([Rob-Johnson](https://github.com/Rob-Johnson))
- \[wip\] use dh-virtualenv to package tron [\#324](https://github.com/Yelp/Tron/pull/324) ([Rob-Johnson](https://github.com/Rob-Johnson))
- \[wip\] start working on a docker env [\#322](https://github.com/Yelp/Tron/pull/322) ([Rob-Johnson](https://github.com/Rob-Johnson))
- Use tox for running tests [\#320](https://github.com/Yelp/Tron/pull/320) ([solarkennedy](https://github.com/solarkennedy))
- only keep last buffer from ssh connection [\#319](https://github.com/Yelp/Tron/pull/319) ([yyejun](https://github.com/yyejun))

## [v0.6.2.0](https://github.com/Yelp/Tron/tree/v0.6.2.0) (2016-08-08)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.1.12...v0.6.2.0)

**Merged pull requests:**

- Add 'hour' to the command context [\#318](https://github.com/Yelp/Tron/pull/318) ([solarkennedy](https://github.com/solarkennedy))

## [v0.6.1.12](https://github.com/Yelp/Tron/tree/v0.6.1.12) (2016-01-07)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.1.5...v0.6.1.12)

**Closed issues:**

- Problem with first start trond [\#308](https://github.com/Yelp/Tron/issues/308)
- tron job 'open failed' errors [\#302](https://github.com/Yelp/Tron/issues/302)

**Merged pull requests:**

- extra cleanup after twisted ssh channel close [\#317](https://github.com/Yelp/Tron/pull/317) ([yyejun](https://github.com/yyejun))
- fix event memory leak [\#316](https://github.com/Yelp/Tron/pull/316) ([yyejun](https://github.com/yyejun))
- Remove non-JSON output [\#314](https://github.com/Yelp/Tron/pull/314) ([pkoch](https://github.com/pkoch))
- More bells and whistles on find\_forgotten\_procs.py [\#313](https://github.com/Yelp/Tron/pull/313) ([pkoch](https://github.com/pkoch))
- Introduce find\_forgotten\_procs.py [\#312](https://github.com/Yelp/Tron/pull/312) ([pkoch](https://github.com/pkoch))
- Fixing build failure [\#311](https://github.com/Yelp/Tron/pull/311) ([tsheasha](https://github.com/tsheasha))
- Add job and service support fields: owner, summary, notes. [\#310](https://github.com/Yelp/Tron/pull/310) ([mikepea](https://github.com/mikepea))
- Vagrant 'development playground' environment [\#304](https://github.com/Yelp/Tron/pull/304) ([mikepea](https://github.com/mikepea))
- Service monitor task should be requeued before notify [\#301](https://github.com/Yelp/Tron/pull/301) ([yyejun](https://github.com/yyejun))
- optimize dashboard fetch api [\#299](https://github.com/Yelp/Tron/pull/299) ([yyejun](https://github.com/yyejun))
- Fix exceptions [\#298](https://github.com/Yelp/Tron/pull/298) ([yyejun](https://github.com/yyejun))
- Fix service restore [\#297](https://github.com/Yelp/Tron/pull/297) ([yyejun](https://github.com/yyejun))
- Redo pull 288 [\#296](https://github.com/Yelp/Tron/pull/296) ([yyejun](https://github.com/yyejun))
- Do not raise on duplicated run id [\#295](https://github.com/Yelp/Tron/pull/295) ([yyejun](https://github.com/yyejun))
- Ignore error in start task [\#288](https://github.com/Yelp/Tron/pull/288) ([yyejun](https://github.com/yyejun))

## [v0.6.1.5](https://github.com/Yelp/Tron/tree/v0.6.1.5) (2014-07-03)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.1.2...v0.6.1.5)

**Closed issues:**

- Skipping an action causes dependant actions to run before scheduled time [\#279](https://github.com/Yelp/Tron/issues/279)

**Merged pull requests:**

- Fix monitor task requeue [\#293](https://github.com/Yelp/Tron/pull/293) ([yyejun](https://github.com/yyejun))
- Fix a but in service monitor failure [\#291](https://github.com/Yelp/Tron/pull/291) ([yyejun](https://github.com/yyejun))
- increase channel start timeout [\#290](https://github.com/Yelp/Tron/pull/290) ([yyejun](https://github.com/yyejun))
- Fix incorrect failure handling [\#287](https://github.com/Yelp/Tron/pull/287) ([yyejun](https://github.com/yyejun))
- report queued job as unknown [\#284](https://github.com/Yelp/Tron/pull/284) ([yyejun](https://github.com/yyejun))
- fix tests failure caused by new default monitor\_retries config [\#283](https://github.com/Yelp/Tron/pull/283) ([yyejun](https://github.com/yyejun))
- Fix more reconnection bug in node service stop [\#282](https://github.com/Yelp/Tron/pull/282) ([yyejun](https://github.com/yyejun))
- Update action\_run state change handling to avoid starting actions before... [\#281](https://github.com/Yelp/Tron/pull/281) ([kesre](https://github.com/kesre))
- fix setup.py packages [\#280](https://github.com/Yelp/Tron/pull/280) ([yyejun](https://github.com/yyejun))

## [v0.6.1.2](https://github.com/Yelp/Tron/tree/v0.6.1.2) (2014-01-14)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.1.1...v0.6.1.2)

**Fixed bugs:**

- Changing count of a service in tronfig requires tronctl start [\#266](https://github.com/Yelp/Tron/issues/266)
- KeyError in 0.6.1 release [\#256](https://github.com/Yelp/Tron/issues/256)
- Service state uses node hostname [\#252](https://github.com/Yelp/Tron/issues/252)
- incorrect tronctl command results in a traceback [\#248](https://github.com/Yelp/Tron/issues/248)

**Closed issues:**

- tron.serialize.filehandler ERROR Could not tail, Cannot allocate memory [\#276](https://github.com/Yelp/Tron/issues/276)
- Add a make task for style checking [\#255](https://github.com/Yelp/Tron/issues/255)

**Merged pull requests:**

- Handle service node not responding to monitor [\#277](https://github.com/Yelp/Tron/pull/277) ([yyejun](https://github.com/yyejun))
- Fix to service count reconfiguration [\#273](https://github.com/Yelp/Tron/pull/273) ([Codeacious](https://github.com/Codeacious))
- Quick fix to JSON Serialization [\#267](https://github.com/Yelp/Tron/pull/267) ([Codeacious](https://github.com/Codeacious))
- Fixed SSHAuthOptions to compare against something that Twisted won't touch [\#265](https://github.com/Yelp/Tron/pull/265) ([Codeacious](https://github.com/Codeacious))
- Fix to configuration loads with %\(month\[+\-\]\[1-12\]\)s that go out of range [\#264](https://github.com/Yelp/Tron/pull/264) ([Codeacious](https://github.com/Codeacious))
- Made service reconfiguration slightly better [\#263](https://github.com/Yelp/Tron/pull/263) ([Codeacious](https://github.com/Codeacious))
- ServiceInstanceMonitorTask.fail fix [\#262](https://github.com/Yelp/Tron/pull/262) ([Codeacious](https://github.com/Codeacious))
- A simple Makefile task for PEP8/PyFlakes checking [\#261](https://github.com/Yelp/Tron/pull/261) ([Codeacious](https://github.com/Codeacious))
- Fixed service data to use node.name, with backwards compatibility [\#260](https://github.com/Yelp/Tron/pull/260) ([Codeacious](https://github.com/Codeacious))
- ssh reconnecting, fix to keyerrors [\#259](https://github.com/Yelp/Tron/pull/259) ([Codeacious](https://github.com/Codeacious))
- Implemented \#221, called tronstore [\#258](https://github.com/Yelp/Tron/pull/258) ([Codeacious](https://github.com/Codeacious))
- First pass at refactoring the Job class structure [\#253](https://github.com/Yelp/Tron/pull/253) ([Codeacious](https://github.com/Codeacious))

## [v0.6.1.1](https://github.com/Yelp/Tron/tree/v0.6.1.1) (2013-07-10)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.6.0.2...v0.6.1.1)

**Closed issues:**

- Attempting to run tron on Illumos-based system [\#246](https://github.com/Yelp/Tron/issues/246)
- tronview should accept a --namespace argument [\#236](https://github.com/Yelp/Tron/issues/236)
- ActionRun history view for tronweb [\#231](https://github.com/Yelp/Tron/issues/231)
- twisted 13.0.0 incompatible with current version of tron [\#227](https://github.com/Yelp/Tron/issues/227)
- cleanup interface for tron.commands.client.Client [\#222](https://github.com/Yelp/Tron/issues/222)
- Ensure Tron follows FHS with its default directory names [\#181](https://github.com/Yelp/Tron/issues/181)
- tronview should accept negative run numbers for most recents [\#173](https://github.com/Yelp/Tron/issues/173)
- Incorrect job end\_time while job is running [\#164](https://github.com/Yelp/Tron/issues/164)
- Add support for a max\_runtime [\#155](https://github.com/Yelp/Tron/issues/155)
- Add jitter parameter to schedulers [\#136](https://github.com/Yelp/Tron/issues/136)
- Split tron.web from main repo [\#117](https://github.com/Yelp/Tron/issues/117)
- Generate a timeline report in image or text format [\#97](https://github.com/Yelp/Tron/issues/97)
- Job status filters [\#85](https://github.com/Yelp/Tron/issues/85)
- Need support for killing a running job [\#31](https://github.com/Yelp/Tron/issues/31)

**Merged pull requests:**

- Fix dev docs [\#254](https://github.com/Yelp/Tron/pull/254) ([dnephin](https://github.com/dnephin))
- Implemented the --namespace argument for tronview \(\#236\) [\#251](https://github.com/Yelp/Tron/pull/251) ([Codeacious](https://github.com/Codeacious))
- Update API urls [\#242](https://github.com/Yelp/Tron/pull/242) ([dnephin](https://github.com/dnephin))
- Fix default config filename, and add a test. [\#241](https://github.com/Yelp/Tron/pull/241) ([dnephin](https://github.com/dnephin))
- Additional end to end tests around state restore [\#240](https://github.com/Yelp/Tron/pull/240) ([dnephin](https://github.com/dnephin))
- Node run error on service instance [\#239](https://github.com/Yelp/Tron/pull/239) ([dnephin](https://github.com/dnephin))
- tronweb - timeline graph and style [\#238](https://github.com/Yelp/Tron/pull/238) ([dnephin](https://github.com/dnephin))
- Tronfig cleanup [\#237](https://github.com/Yelp/Tron/pull/237) ([dnephin](https://github.com/dnephin))
- JS Unit testing and more tronweb UI [\#234](https://github.com/Yelp/Tron/pull/234) ([dnephin](https://github.com/dnephin))
- tronweb re-style [\#230](https://github.com/Yelp/Tron/pull/230) ([dnephin](https://github.com/dnephin))
- force kill service [\#229](https://github.com/Yelp/Tron/pull/229) ([dnephin](https://github.com/dnephin))
- command client interface [\#226](https://github.com/Yelp/Tron/pull/226) ([dnephin](https://github.com/dnephin))
- Services with monitoring instances are still up. [\#225](https://github.com/Yelp/Tron/pull/225) ([dnephin](https://github.com/dnephin))
- max runtime for jobs [\#224](https://github.com/Yelp/Tron/pull/224) ([dnephin](https://github.com/dnephin))
- negative numbers for job run [\#220](https://github.com/Yelp/Tron/pull/220) ([dnephin](https://github.com/dnephin))
- Move some ssh option constants to the config [\#219](https://github.com/Yelp/Tron/pull/219) ([dnephin](https://github.com/dnephin))
- The new tronweb - Yelp hackathon 10 [\#218](https://github.com/Yelp/Tron/pull/218) ([dnephin](https://github.com/dnephin))
- Kill a running action [\#214](https://github.com/Yelp/Tron/pull/214) ([dnephin](https://github.com/dnephin))
- scheduler jitter [\#213](https://github.com/Yelp/Tron/pull/213) ([dnephin](https://github.com/dnephin))
- correct end\_time for running jobs. [\#212](https://github.com/Yelp/Tron/pull/212) ([dnephin](https://github.com/dnephin))

## [v0.6.0.2](https://github.com/Yelp/Tron/tree/v0.6.0.2) (2013-04-04)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.2.3...v0.6.0.2)

**Fixed bugs:**

- Cancelling a JobRun can trigger some actions to run [\#202](https://github.com/Yelp/Tron/issues/202)
- Service state can be UP even when no instances are active [\#139](https://github.com/Yelp/Tron/issues/139)
- Failure during reconfig could cause inconsistent service state [\#38](https://github.com/Yelp/Tron/issues/38)

**Closed issues:**

- Support host key verification [\#199](https://github.com/Yelp/Tron/issues/199)
- Connection failure error message should be recorded in stderr [\#184](https://github.com/Yelp/Tron/issues/184)
- Some docs still refer to succeed [\#175](https://github.com/Yelp/Tron/issues/175)
- Refactor event module [\#142](https://github.com/Yelp/Tron/issues/142)
- Provide a read-only REST interface [\#110](https://github.com/Yelp/Tron/issues/110)
- Services can get stuck in STOPPING [\#96](https://github.com/Yelp/Tron/issues/96)
- Improve service view from tronview [\#51](https://github.com/Yelp/Tron/issues/51)

**Merged pull requests:**

- 0.6.0.2, better handling for service instance monitoring [\#215](https://github.com/Yelp/Tron/pull/215) ([dnephin](https://github.com/dnephin))
- Release 0.6.0.1 bug fixes [\#211](https://github.com/Yelp/Tron/pull/211) ([dnephin](https://github.com/dnephin))
- debugging and testing [\#210](https://github.com/Yelp/Tron/pull/210) ([dnephin](https://github.com/dnephin))
- 0.6 replace reactor with eventloop [\#209](https://github.com/Yelp/Tron/pull/209) ([dnephin](https://github.com/dnephin))
- Verify Host Key and SSH config options [\#207](https://github.com/Yelp/Tron/pull/207) ([dnephin](https://github.com/dnephin))
- node pool and event cleanup [\#206](https://github.com/Yelp/Tron/pull/206) ([dnephin](https://github.com/dnephin))
- Log an informative error when we're missing a local channel. [\#205](https://github.com/Yelp/Tron/pull/205) ([dnephin](https://github.com/dnephin))
- Cleanup around API responses, scheduler config, etc [\#204](https://github.com/Yelp/Tron/pull/204) ([dnephin](https://github.com/dnephin))
- Resolve \#202 and add a unit test and acceptance test. [\#203](https://github.com/Yelp/Tron/pull/203) ([dnephin](https://github.com/dnephin))
- JobCollection and additional details in tronview [\#201](https://github.com/Yelp/Tron/pull/201) ([dnephin](https://github.com/dnephin))
- Update docs and pull out some logic from tron.api.www [\#200](https://github.com/Yelp/Tron/pull/200) ([dnephin](https://github.com/dnephin))
- Service Refactor [\#197](https://github.com/Yelp/Tron/pull/197) ([dnephin](https://github.com/dnephin))

## [v0.5.2.3](https://github.com/Yelp/Tron/tree/v0.5.2.3) (2013-02-15)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.2.2...v0.5.2.3)

**Closed issues:**

- Separate view and control APIs [\#147](https://github.com/Yelp/Tron/issues/147)
- Maximum queue length job config option [\#130](https://github.com/Yelp/Tron/issues/130)
- Retry failed jobs [\#86](https://github.com/Yelp/Tron/issues/86)

**Merged pull requests:**

- Support other users [\#198](https://github.com/Yelp/Tron/pull/198) ([dnephin](https://github.com/dnephin))

## [v0.5.2.2](https://github.com/Yelp/Tron/tree/v0.5.2.2) (2013-02-12)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.1...v0.5.2.2)

**Fixed bugs:**

- Reconfigure after disable/enable can result in incorrect run time for scheduled job [\#195](https://github.com/Yelp/Tron/issues/195)

**Closed issues:**

- Preserve config format/comments on tronfig [\#189](https://github.com/Yelp/Tron/issues/189)
- disabling queueing should not immediately schedule all queued jobs [\#187](https://github.com/Yelp/Tron/issues/187)
- Separate Tron unit tests from functional testing, using mocks where appropriate [\#182](https://github.com/Yelp/Tron/issues/182)
- A job consists of a list of actions,could I run actions in different nodes? [\#176](https://github.com/Yelp/Tron/issues/176)
- rescheduling a job schedules a run for the wrong time [\#174](https://github.com/Yelp/Tron/issues/174)
- Updating configs should be event-driven [\#80](https://github.com/Yelp/Tron/issues/80)
- Allow for Tron to use multiple config files [\#30](https://github.com/Yelp/Tron/issues/30)

**Merged pull requests:**

- 195 scheduling after reconfigure [\#196](https://github.com/Yelp/Tron/pull/196) ([dnephin](https://github.com/dnephin))
- 0.5.2 state watcher for reconfigure [\#194](https://github.com/Yelp/Tron/pull/194) ([dnephin](https://github.com/dnephin))
- State migration tools [\#193](https://github.com/Yelp/Tron/pull/193) ([dnephin](https://github.com/dnephin))
- Always initliaze a state machine to it's initial state [\#192](https://github.com/Yelp/Tron/pull/192) ([dnephin](https://github.com/dnephin))
- Add a config hash [\#191](https://github.com/Yelp/Tron/pull/191) ([dnephin](https://github.com/dnephin))
- Support multiple config files [\#190](https://github.com/Yelp/Tron/pull/190) ([dnephin](https://github.com/dnephin))
- Updates to changelog and whats-new files, to reflect a new minor version update [\#188](https://github.com/Yelp/Tron/pull/188) ([y-trobinso](https://github.com/y-trobinso))
- Fix job config docs [\#186](https://github.com/Yelp/Tron/pull/186) ([dnephin](https://github.com/dnephin))
- Add the ability to reconcile configuration fragments to Tron [\#185](https://github.com/Yelp/Tron/pull/185) ([y-trobinso](https://github.com/y-trobinso))
- Adds "make build" and the concept of usernames to node.py [\#183](https://github.com/Yelp/Tron/pull/183) ([y-trobinso](https://github.com/y-trobinso))
- Remove a reference to old config style in docs [\#179](https://github.com/Yelp/Tron/pull/179) ([irskep](https://github.com/irskep))
- Fix exceptions in tronweb [\#178](https://github.com/Yelp/Tron/pull/178) ([Bklyn](https://github.com/Bklyn))
- Red header and footer for docs [\#177](https://github.com/Yelp/Tron/pull/177) ([irskep](https://github.com/irskep))
- Some general cleanup. [\#172](https://github.com/Yelp/Tron/pull/172) ([dnephin](https://github.com/dnephin))

## [v0.5.1](https://github.com/Yelp/Tron/tree/v0.5.1) (2012-07-25)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.0.2...v0.5.1)

**Closed issues:**

- Support cron syntax for schedules [\#28](https://github.com/Yelp/Tron/issues/28)

**Merged pull requests:**

- Cron Scheduler [\#169](https://github.com/Yelp/Tron/pull/169) ([dnephin](https://github.com/dnephin))

## [v0.5.0.2](https://github.com/Yelp/Tron/tree/v0.5.0.2) (2012-07-18)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.0.1...v0.5.0.2)

**Fixed bugs:**

- Prevent starting individual actions [\#158](https://github.com/Yelp/Tron/issues/158)

**Closed issues:**

- jobs should not automatically re-enable with config updates [\#160](https://github.com/Yelp/Tron/issues/160)
- Remove deprecated config options [\#140](https://github.com/Yelp/Tron/issues/140)
- Stop using twistd [\#119](https://github.com/Yelp/Tron/issues/119)
- Graceful shutdown [\#113](https://github.com/Yelp/Tron/issues/113)
- Unify various directory/location command line switches [\#112](https://github.com/Yelp/Tron/issues/112)
- Store state in sqlite [\#111](https://github.com/Yelp/Tron/issues/111)
- Let jobs overlap if user says so [\#43](https://github.com/Yelp/Tron/issues/43)

**Merged pull requests:**

- Fix reactor in daemon [\#170](https://github.com/Yelp/Tron/pull/170) ([dnephin](https://github.com/dnephin))
- Allow jobs to overlap [\#168](https://github.com/Yelp/Tron/pull/168) ([dnephin](https://github.com/dnephin))
- Do not allow actions to be manually started if their job run is still scheduled [\#166](https://github.com/Yelp/Tron/pull/166) ([dnephin](https://github.com/dnephin))
- Preserve job enabled. [\#165](https://github.com/Yelp/Tron/pull/165) ([dnephin](https://github.com/dnephin))

## [v0.5.0.1](https://github.com/Yelp/Tron/tree/v0.5.0.1) (2012-06-19)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.5.0...v0.5.0.1)

**Merged pull requests:**

- Support legacy state files. [\#163](https://github.com/Yelp/Tron/pull/163) ([dnephin](https://github.com/dnephin))
- State serialization and tron daemon [\#148](https://github.com/Yelp/Tron/pull/148) ([dnephin](https://github.com/dnephin))

## [v0.5.0](https://github.com/Yelp/Tron/tree/v0.5.0) (2012-06-19)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.4.1.1...v0.5.0)

**Closed issues:**

- Remove pending on reconfigure fails [\#161](https://github.com/Yelp/Tron/issues/161)

**Merged pull requests:**

- Fix for missing format specifier [\#162](https://github.com/Yelp/Tron/pull/162) ([ninsen](https://github.com/ninsen))

## [v0.4.1.1](https://github.com/Yelp/Tron/tree/v0.4.1.1) (2012-05-31)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.4.1...v0.4.1.1)

## [v0.4.1](https://github.com/Yelp/Tron/tree/v0.4.1) (2012-05-30)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.4.0...v0.4.1)

**Closed issues:**

- time monkeypatching should be done under tests/ [\#141](https://github.com/Yelp/Tron/issues/141)
- Fix testing sandbox [\#125](https://github.com/Yelp/Tron/issues/125)

**Merged pull requests:**

- Manually cancelled jobs should still continue to schedule new runs. [\#159](https://github.com/Yelp/Tron/pull/159) ([dnephin](https://github.com/dnephin))
- Fix testing sandbox [\#157](https://github.com/Yelp/Tron/pull/157) ([dnephin](https://github.com/dnephin))
- Release 0.4.1 [\#156](https://github.com/Yelp/Tron/pull/156) ([dnephin](https://github.com/dnephin))
- Enabled should not be part of job equality test. [\#154](https://github.com/Yelp/Tron/pull/154) ([dnephin](https://github.com/dnephin))
- Handle no tty size gracefully. [\#152](https://github.com/Yelp/Tron/pull/152) ([dnephin](https://github.com/dnephin))
- Release 0.4.0.2 [\#151](https://github.com/Yelp/Tron/pull/151) ([dnephin](https://github.com/dnephin))
- Fix state restore from old state files. [\#150](https://github.com/Yelp/Tron/pull/150) ([dnephin](https://github.com/dnephin))
- fix debian/changelog formatting [\#149](https://github.com/Yelp/Tron/pull/149) ([Roguelazer](https://github.com/Roguelazer))

## [v0.4.0](https://github.com/Yelp/Tron/tree/v0.4.0) (2012-05-14)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.3.3...v0.4.0)

**Fixed bugs:**

- Actions not dependent on a failed action should still run [\#118](https://github.com/Yelp/Tron/issues/118)
- error on shutdown [\#114](https://github.com/Yelp/Tron/issues/114)
- Re-enabling a disabled daily job unexpectedly schedules it [\#36](https://github.com/Yelp/Tron/issues/36)

**Closed issues:**

- Date alias for last successful action run [\#122](https://github.com/Yelp/Tron/issues/122)

**Merged pull requests:**

- Update the docs and changed the docs theme [\#146](https://github.com/Yelp/Tron/pull/146) ([dnephin](https://github.com/dnephin))
- Action Dependency Diagram [\#145](https://github.com/Yelp/Tron/pull/145) ([dnephin](https://github.com/dnephin))
- Bug fixes for job refactor [\#144](https://github.com/Yelp/Tron/pull/144) ([dnephin](https://github.com/dnephin))
- alter debian packaging to handle logging.conf better [\#137](https://github.com/Yelp/Tron/pull/137) ([Roguelazer](https://github.com/Roguelazer))
- Job Scheduling Refactor [\#134](https://github.com/Yelp/Tron/pull/134) ([dnephin](https://github.com/dnephin))

## [v0.3.3](https://github.com/Yelp/Tron/tree/v0.3.3) (2012-04-19)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.3.2...v0.3.3)

**Fixed bugs:**

- Strange behavior for stuck jobs after reconfig [\#40](https://github.com/Yelp/Tron/issues/40)

**Closed issues:**

- Resolve warnings on \(re\)config about working directory [\#131](https://github.com/Yelp/Tron/issues/131)
- Config file convert script 0.2.x -\> 0.3.x [\#109](https://github.com/Yelp/Tron/issues/109)
- File system resources [\#26](https://github.com/Yelp/Tron/issues/26)

**Merged pull requests:**

- Configuration migration from 0.2 to 0.3 [\#133](https://github.com/Yelp/Tron/pull/133) ([dnephin](https://github.com/dnephin))
- 131 resolve wd warning [\#132](https://github.com/Yelp/Tron/pull/132) ([dnephin](https://github.com/dnephin))
- Release 0.3.2 [\#129](https://github.com/Yelp/Tron/pull/129) ([dnephin](https://github.com/dnephin))

## [v0.3.2](https://github.com/Yelp/Tron/tree/v0.3.2) (2012-04-12)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.3.1...v0.3.2)

**Fixed bugs:**

- Problems after upgrade to 0.3.0/0.3.1 [\#127](https://github.com/Yelp/Tron/issues/127)

**Closed issues:**

- Support only logging to syslog [\#115](https://github.com/Yelp/Tron/issues/115)

**Merged pull requests:**

- Additional node pool validation [\#128](https://github.com/Yelp/Tron/pull/128) ([dnephin](https://github.com/dnephin))
- 115 move logging to config file [\#126](https://github.com/Yelp/Tron/pull/126) ([dnephin](https://github.com/dnephin))

## [v0.3.1](https://github.com/Yelp/Tron/tree/v0.3.1) (2012-03-27)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.3.0...v0.3.1)

**Closed issues:**

- Let command context variables use built-in interpolations [\#101](https://github.com/Yelp/Tron/issues/101)
- Look into making CommandContext more like django contexts [\#33](https://github.com/Yelp/Tron/issues/33)

**Merged pull requests:**

- Run all actions, even if a non-dependent action fails [\#124](https://github.com/Yelp/Tron/pull/124) ([dnephin](https://github.com/dnephin))
- Fix cleanup actions. [\#123](https://github.com/Yelp/Tron/pull/123) ([dnephin](https://github.com/dnephin))
- State diagrams [\#121](https://github.com/Yelp/Tron/pull/121) ([dnephin](https://github.com/dnephin))
- Remove req.txt [\#116](https://github.com/Yelp/Tron/pull/116) ([dnephin](https://github.com/dnephin))

## [v0.3.0](https://github.com/Yelp/Tron/tree/v0.3.0) (2012-03-21)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.10...v0.3.0)

**Fixed bugs:**

- Cleanup actions break IntervalScheduler [\#91](https://github.com/Yelp/Tron/issues/91)

**Closed issues:**

- Failed to connect to host [\#95](https://github.com/Yelp/Tron/issues/95)
- No-op scheduler [\#88](https://github.com/Yelp/Tron/issues/88)
- Cannot restart failed actions [\#87](https://github.com/Yelp/Tron/issues/87)
- Nodes and node pools should be in separate lists [\#69](https://github.com/Yelp/Tron/issues/69)
- Action.requires should accept strings in the list as well as pointers [\#61](https://github.com/Yelp/Tron/issues/61)
- support a global /etc/tron [\#60](https://github.com/Yelp/Tron/issues/60)
- 'tronctl succeed' should allow FAIL -\> SUCC [\#45](https://github.com/Yelp/Tron/issues/45)
- Jobs, actions, nodes, etc. should support string identifiers alongside YAML references [\#44](https://github.com/Yelp/Tron/issues/44)
- retry\_count config option [\#27](https://github.com/Yelp/Tron/issues/27)

**Merged pull requests:**

- Docs and make [\#108](https://github.com/Yelp/Tron/pull/108) ([dnephin](https://github.com/dnephin))
- Tronview tests and bugs fixes [\#107](https://github.com/Yelp/Tron/pull/107) ([dnephin](https://github.com/dnephin))
- Fds should be closed [\#106](https://github.com/Yelp/Tron/pull/106) ([dnephin](https://github.com/dnephin))
- Job can be configured disabled [\#105](https://github.com/Yelp/Tron/pull/105) ([dnephin](https://github.com/dnephin))
- Tronview cleanup [\#104](https://github.com/Yelp/Tron/pull/104) ([dnephin](https://github.com/dnephin))
- Config rewrite [\#103](https://github.com/Yelp/Tron/pull/103) ([dnephin](https://github.com/dnephin))
- Config rewrite [\#90](https://github.com/Yelp/Tron/pull/90) ([irskep](https://github.com/irskep))

## [v0.2.10](https://github.com/Yelp/Tron/tree/v0.2.10) (2012-02-17)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.9...v0.2.10)

**Closed issues:**

- Bug? unsupported format character [\#84](https://github.com/Yelp/Tron/issues/84)
- Failed service starts should show output somewhere [\#37](https://github.com/Yelp/Tron/issues/37)
- Revisit Action "requires" field [\#29](https://github.com/Yelp/Tron/issues/29)

**Merged pull requests:**

- Cleanup actions don't disable job on interval scheduler when an action fails [\#94](https://github.com/Yelp/Tron/pull/94) ([irskep](https://github.com/irskep))
- Remove old man [\#93](https://github.com/Yelp/Tron/pull/93) ([dnephin](https://github.com/dnephin))
- Support skipping of failed actions [\#92](https://github.com/Yelp/Tron/pull/92) ([dnephin](https://github.com/dnephin))
- Pyflakes cleanup [\#89](https://github.com/Yelp/Tron/pull/89) ([dnephin](https://github.com/dnephin))

## [v0.2.9](https://github.com/Yelp/Tron/tree/v0.2.9) (2012-02-06)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.8.1...v0.2.9)

**Fixed bugs:**

- Failed first action of two-action job stops scheduler [\#77](https://github.com/Yelp/Tron/issues/77)
- Syslog reconfig doesn't take effect until daemon restart [\#66](https://github.com/Yelp/Tron/issues/66)
- Tron and DST do not get along [\#59](https://github.com/Yelp/Tron/issues/59)

**Closed issues:**

- tronweb is broken [\#75](https://github.com/Yelp/Tron/issues/75)
- Working TronWeb UI \(for viewing jobs\) [\#72](https://github.com/Yelp/Tron/issues/72)
- Handle dependencies and failures between dependencies better [\#67](https://github.com/Yelp/Tron/issues/67)

**Merged pull requests:**

- Jobs no longer stop scheduling when non-final action fails after next scheduled run [\#79](https://github.com/Yelp/Tron/pull/79) ([irskep](https://github.com/irskep))
- Kill reactor so test suite can exit [\#76](https://github.com/Yelp/Tron/pull/76) ([irskep](https://github.com/irskep))
- Tronweb 72 [\#74](https://github.com/Yelp/Tron/pull/74) ([mowings-iseatz](https://github.com/mowings-iseatz))
- Daylight Saving Time Awareness \(\#59\) \(fixed target branch\) [\#71](https://github.com/Yelp/Tron/pull/71) ([irskep](https://github.com/irskep))
- Comments and style [\#68](https://github.com/Yelp/Tron/pull/68) ([irskep](https://github.com/irskep))

## [v0.2.8.1](https://github.com/Yelp/Tron/tree/v0.2.8.1) (2011-12-21)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.8...v0.2.8.1)

**Fixed bugs:**

- Update incorrect documentation [\#50](https://github.com/Yelp/Tron/issues/50)

**Closed issues:**

- Unified HTML documentation [\#49](https://github.com/Yelp/Tron/issues/49)
- System for emailing job failures [\#34](https://github.com/Yelp/Tron/issues/34)

**Merged pull requests:**

- Prebuilt man pages [\#65](https://github.com/Yelp/Tron/pull/65) ([irskep](https://github.com/irskep))
- better formatting when logging to syslog [\#63](https://github.com/Yelp/Tron/pull/63) ([Roguelazer](https://github.com/Roguelazer))

## [v0.2.8](https://github.com/Yelp/Tron/tree/v0.2.8) (2011-11-28)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.7...v0.2.8)

**Fixed bugs:**

- tron exception [\#46](https://github.com/Yelp/Tron/issues/46)
- NameError in www.py [\#22](https://github.com/Yelp/Tron/issues/22)

**Closed issues:**

- Scheduled Time seem inconsistent [\#54](https://github.com/Yelp/Tron/issues/54)
- tronfig should disallow putting Jobs in the services list [\#47](https://github.com/Yelp/Tron/issues/47)
- support logging to syslog [\#41](https://github.com/Yelp/Tron/issues/41)
- Add a "zap" command for services [\#39](https://github.com/Yelp/Tron/issues/39)
- trond silently fails when run as non-root user  [\#13](https://github.com/Yelp/Tron/issues/13)

**Merged pull requests:**

- Docs and more [\#62](https://github.com/Yelp/Tron/pull/62) ([irskep](https://github.com/irskep))
- Logging to syslog \(\#41\) [\#58](https://github.com/Yelp/Tron/pull/58) ([irskep](https://github.com/irskep))
- more fixen [\#57](https://github.com/Yelp/Tron/pull/57) ([Roguelazer](https://github.com/Roguelazer))
- make config parsing better [\#55](https://github.com/Yelp/Tron/pull/55) ([Roguelazer](https://github.com/Roguelazer))
- Zap command for services \(\#39\) [\#53](https://github.com/Yelp/Tron/pull/53) ([irskep](https://github.com/irskep))
- Make tronview more resilient to bad tronfigs [\#48](https://github.com/Yelp/Tron/pull/48) ([Roguelazer](https://github.com/Roguelazer))
- added missing import and fixed import ordering [\#24](https://github.com/Yelp/Tron/pull/24) ([tobywaite](https://github.com/tobywaite))
- Cleanup actions [\#16](https://github.com/Yelp/Tron/pull/16) ([irskep](https://github.com/irskep))

## [v0.2.7](https://github.com/Yelp/Tron/tree/v0.2.7) (2011-09-14)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.6...v0.2.7)

## [v0.2.6](https://github.com/Yelp/Tron/tree/v0.2.6) (2011-09-14)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.5...v0.2.6)

**Closed issues:**

- Failure actions for jobs [\#14](https://github.com/Yelp/Tron/issues/14)

**Merged pull requests:**

- Functional testing improvements [\#21](https://github.com/Yelp/Tron/pull/21) ([irskep](https://github.com/irskep))
- Fancy new scheduler based on Google App Engine's [\#20](https://github.com/Yelp/Tron/pull/20) ([irskep](https://github.com/irskep))
- TronTestCase: functional testing! [\#18](https://github.com/Yelp/Tron/pull/18) ([irskep](https://github.com/irskep))
- Added context variables for year, month, day [\#17](https://github.com/Yelp/Tron/pull/17) ([irskep](https://github.com/irskep))

## [v0.2.5](https://github.com/Yelp/Tron/tree/v0.2.5) (2011-06-23)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.4...v0.2.5)

## [v0.2.4](https://github.com/Yelp/Tron/tree/v0.2.4) (2011-04-12)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.2.0...v0.2.4)

## [v0.2.0](https://github.com/Yelp/Tron/tree/v0.2.0) (2011-02-25)
[Full Changelog](https://github.com/Yelp/Tron/compare/v0.1.10...v0.2.0)

## [v0.1.10](https://github.com/Yelp/Tron/tree/v0.1.10) (2011-02-03)
[Full Changelog](https://github.com/Yelp/Tron/compare/0.1.9...v0.1.10)

## [0.1.9](https://github.com/Yelp/Tron/tree/0.1.9) (2010-12-14)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
