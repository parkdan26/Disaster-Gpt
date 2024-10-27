import Navbar from "./components/navbar";
import Signup from "./components/signup";
import bgvideo from "./components/images/broll.mp4";

export default function App() {
  return (
    <div className='h-[100vh] m-0 p-0'>
      <video className='absolute top-0 left-0 h-[100vh] w-[100vw] object-cover -z-10' loop autoPlay muted>
        <source src={bgvideo} type="video/mp4" />
      </video>
      <Navbar />
      <Signup />
    </div>
  );
}