import { LeaderboardTable } from "@/components/templates/leaderboar-table/indext";

export default function Home() {
    return (
        <div className="m-auto my-10 max-w-xl max-md:mx-2">
            <LeaderboardTable data={[]} />
        </div>
    );
}
